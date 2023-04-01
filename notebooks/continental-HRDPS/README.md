The Jupyter Notebooks in this directory are made by
Doug Latornell for sharing of Python code techniques
and notes.
They are about processing of the ECCC MSC continental grid 2.5 km HRDPS GRIB2 files
to create NEMO atmospheric forcing files for SalishSeaCast.

The links below are to static renderings of the notebooks via
[nbviewer.jupyter.org](https://nbviewer.org/).
Descriptions below the links are from the first cell of the notebooks
(if that cell contains Markdown or raw text).

* ## [cfgrib-grib_to_netcdf.ipynb](https://nbviewer.org/github/SalishSeaCast/analysis-doug/blob/main/notebooks/continental-HRDPS/cfgrib-grib_to_netcdf.ipynb)  
    
    **`grib_to_netcdf` Processing of Continental HRDPS with `cfgrib`**
    
    Exploration of doing the processing of the SalishSeaNowcast `grib_to_netcdf` worker
    to generate NEMO atmospheric forcing files for SalishSeaCast from the
    ECCC MSC 2.5 km rotated lat-lon continental grid HRDPS GRIB2 files using the `cfgrib` package.

* ## [crop-grib-to-SSC-domain.ipynb.ipynb](https://nbviewer.org/github/SalishSeaCast/analysis-doug/blob/main/notebooks/continental-HRDPS/crop-grib-to-SSC-domain.ipynb.ipynb)  
    
    **Crop HRDPS Continental GRIB2 File with `xarray` and `cfgrib`**
    
    Exploration of loading a ECCC MSC 2.5 km rotated lat-lon continental grid HRDPS GRIB2 file,
    cropping it to the sub-domain needed for SalishSeaCast NEMO forcing,
    and writing it to a new GRIB2 file.

* ## [make-SSC_grid_georef-nc.ipynb](https://nbviewer.org/github/SalishSeaCast/analysis-doug/blob/main/notebooks/continental-HRDPS/make-SSC_grid_georef-nc.ipynb)  
    
    **Create `SSC_grid_georef.nc` File**
    
    Please see 
    https://nbviewer.org/github/SalishSeaCast/analysis-doug/blob/main/notebooks/continental-HRDPS/crop-grib-to-SSC-domain.ipynb.ipynb
    for the story behind why this file is needed.

* ## [pywgrib2-grib_to_netcdf.ipynb](https://nbviewer.org/github/SalishSeaCast/analysis-doug/blob/main/notebooks/continental-HRDPS/pywgrib2-grib_to_netcdf.ipynb)  
    
    **`grib_to_netcdf` Processing of Continental HRDPS with `pywgrib2_xr`**
    
    Exploration of doing the processing of the SalishSeaNowcast `grib_to_netcdf` worker
    to generate NEMO atmospheric forcing files for SalishSeaCast from the
    ECCC MSC 2.5 km rotated lat-lon continental grid HRDPS GRIB2 files using the `pywgrib2_xr` package.


## License

These notebooks and files are copyright by the
[UBC EOAS MOAD Group](https://github.com/UBC-MOAD/docs/blob/master/CONTRIBUTORS.rst)
and The University of British Columbia.

They are licensed under the Apache License, Version 2.0.
https://www.apache.org/licenses/LICENSE-2.0
Please see the LICENSE file in this repository for details of the license.
