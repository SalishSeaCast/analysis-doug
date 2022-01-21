The Jupyter Notebooks in this directory are made by
Doug Latornell for sharing of Python code techniques
and notes.

The links below are to static renderings of the notebooks via
[nbviewer.org](https://nbviewer.org/).
Descriptions below the links are from the first cell of the notebooks
(if that cell contains Markdown or raw text).

* ## [elise_dask_expts.ipynb](https://nbviewer.org/github/SalishSeaCast/analysis-doug/blob/main/notebooks/dask-expts/elise_dask_expts.ipynb)  
    
    **`dask` Experiments for Elise's Plankton Averaging Workflow**
    
    This notebook explores the performance of `dask` and `xarray.open_mfdataset()` 
    compared to looping over files with `netCDF4` for Elise's diatoms and microzooplankton
    averaging workflow.

* ## [atlantis_nudge_diatoms.ipynb](https://nbviewer.org/github/SalishSeaCast/analysis-doug/blob/main/notebooks/dask-expts/atlantis_nudge_diatoms.ipynb)  
    
    **SSC Diatoms Extraction for Nudging Atlantis**
    
    This notebook explores using `dask.distributed` to extract diatom and lon/lat fields
    from day-averaged SalishSeaCast hindcast files to create long time series files that
    can be processed to generate "nudging" fields for Atlantis.

* ## [timing_decorator.ipynb](https://nbviewer.org/github/SalishSeaCast/analysis-doug/blob/main/notebooks/dask-expts/timing_decorator.ipynb)  
    
    **Function Timing Decorator**
    
    Notes about a simple decorator to time function execution.
    Useful as a replacement for `%%time` cell magic when using `dask`.

* ## [dask_expts.ipynb](https://nbviewer.org/github/SalishSeaCast/analysis-doug/blob/main/notebooks/dask-expts/dask_expts.ipynb)  
    
    **`dask` Experiments on SalishSeaCast Results**
    
    This notebook explores how to use `dask` and `xarray.open_mfdataset()` to
    improve the performance of operations on multiple day's SalishSeaCast results files.


## License

These notebooks and files are copyright by the
[UBC EOAS MOAD Group](https://github.com/UBC-MOAD/docs/blob/master/CONTRIBUTORS.rst)
and The University of British Columbia.

They are licensed under the Apache License, Version 2.0.
http://www.apache.org/licenses/LICENSE-2.0
Please see the LICENSE file in this repository for details of the license.
