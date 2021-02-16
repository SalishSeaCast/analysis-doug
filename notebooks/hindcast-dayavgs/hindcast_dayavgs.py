# Copyright by the UBC EOAS MOAD Group and The University of British Columbia.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Calculate day-averaged variable fields from SalishSeaCast NEMO hour-averaged fields
and store the day-averaged fields in netCDF4 files beside the hour-averaged files.

Dev notebook: SalishSeaCast/analysis-doug/notebooks/hindcast-dayavgs/hindcast-dayavgs-dev.ipynb
"""
from copy import copy
import logging
from pathlib import Path
import sys
import time

import arrow
import numpy
import xarray

logging.getLogger(__name__).addHandler(logging.NullHandler())


HINDCAST_PATH = Path("/results2/SalishSea/nowcast-green.201905")
TRACER_GROUPS = ("grid_T", "carp_T", "ptrc_T")
IN_CHUNKS = {
    "time_counter": 24,
    "deptht": 40,
    "y": 898,
    "x": 398,
}
OUT_CHUNKS = {
    "time_counter": 1,
    "deptht": 40,
    "y": 898,
    "x": 398,
}
OUT_CHUNKS_4D = list(OUT_CHUNKS.values())
OUT_CHUNKS_3D = copy(OUT_CHUNKS_4D)
OUT_CHUNKS_3D.remove(OUT_CHUNKS["deptht"])
DROP_VARS = (
    "axis_nbounds",
    "nvertex",
    "bounds_lon",
    "bounds_lat",
    "bounds_nav_lon",
    "bounds_nav_lat",
    "area",
    "deptht_bounds",
    "time_centered",
    "time_centered_bounds",
    "time_counter_bounds",
)


def hindcast_dayavgs(
    start_date: arrow.Arrow, end_date: arrow.Arrow, n_workers: int
) -> None:
    t_start_total = time.time()
    for day in arrow.Arrow.range("day", start_date, end_date):
        t_start_day = time.time()
        ddmmmyy = day.format("DDMMMYY").lower()
        yyyymmdd = day.format("YYYYMMDD")
        for tracer_group in TRACER_GROUPS:
            t_start_tracer = time.time()
            hour_avgs_file = (
                HINDCAST_PATH
                / f"{ddmmmyy}"
                / f"SalishSea_1h_{yyyymmdd}_{yyyymmdd}_{tracer_group}.nc"
            )
            hour_avgs = xarray.open_dataset(
                hour_avgs_file, chunks=IN_CHUNKS, drop_variables=DROP_VARS
            )
            logging.info(f"opened {hour_avgs_file}")
            day_avgs = hour_avgs.resample(time_counter="D").mean(
                dim="time_counter", skipna=True, keep_attrs=True
            )
            day_avgs.load(scheduler="processes", num_workers=n_workers)
            day_avgs["time_counter"] = day_avgs.time_counter + numpy.timedelta64(
                12, "h"
            )
            _improve_metadata(day_avgs, hour_avgs)
            day_avgs_file = (
                HINDCAST_PATH
                / f"{ddmmmyy}"
                / f"SalishSea_1d_{yyyymmdd}_{yyyymmdd}_{tracer_group}.nc"
            )
            encoding = _calc_encoding(day_avgs, OUT_CHUNKS_4D, OUT_CHUNKS_3D)
            day_avgs.to_netcdf(day_avgs_file, encoding=encoding)
            logging.info(f"wrote {day_avgs_file}")
            logging.debug(f"{ddmmmyy} {tracer_group}: {time.time() - t_start_tracer} s")
        logging.debug(f"{ddmmmyy}: {time.time() - t_start_day} s")
    logging.debug(f"total: {time.time() - t_start_total} s")


def _improve_metadata(day_avgs: xarray.Dataset, hour_avgs: xarray.Dataset) -> None:
    day_avgs.time_counter.attrs.update(
        {
            "time_origin": hour_avgs.time_counter.attrs["time_origin"],
            "standard_name": hour_avgs.time_counter.attrs["standard_name"],
            "long_name": hour_avgs.time_counter.attrs["long_name"],
            "comment": (
                "time_counter values are UTC at the centre of the intervals over which "
                "the calculated model results are averaged"
            ),
            "_NoFill": "true",
        }
    )

    for coord in ("nav_lon", "nav_lat", "deptht"):
        del day_avgs[coord].attrs["bounds"]

    drop_attrs = (
        "online_operation",
        "interval_operation",
        "interval_write",
        "cell_methods",
        "cell_measures",
    )
    for var in day_avgs.data_vars:
        for attr in drop_attrs:
            del day_avgs[var].attrs[attr]


def _calc_encoding(
    day_avgs: xarray.Dataset, out_chunks_4d: list[int], out_chunks_3d: list[int]
) -> dict:
    encoding = {
        var: {
            "zlib": True,
            "chunksizes": out_chunks_4d if day_avgs[var].ndim == 4 else out_chunks_3d,
        }
        for var in day_avgs.data_vars
    }
    encoding["time_counter"] = {
        "dtype": "d",
        "calendar": "gregorian",
        "units": "seconds since 1900-01-01 00:00:00",
        "chunksizes": [1],
        "_FillValue": None,
    }
    return encoding


def _cli(argv: list) -> tuple:
    start_date, end_date, n_workers, verbosity = argv
    start_date, end_date = arrow.get(start_date), arrow.get(end_date)
    n_workers = int(n_workers)
    logging_level = getattr(logging, verbosity.upper())
    logging.basicConfig(
        level=logging_level,
        format="%(asctime)s hindcast_dayavgs %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        stream=sys.stdout,
    )
    return start_date, end_date, n_workers


# This stanza facilitates running the script in a Python debugger
if __name__ == "__main__":
    start_date, end_date, n_workers = _cli(sys.argv[1:])
    hindcast_dayavgs(start_date, end_date, n_workers)
