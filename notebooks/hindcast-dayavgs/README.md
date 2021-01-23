The Jupyter Notebook in this directory are made by
Doug Latornell for sharing of Python code techniques
and notes.

The links below are to static renderings of the notebooks via
[nbviewer.jupyter.org](https://nbviewer.jupyter.org/).
Descriptions below the links are from the first cell of the notebooks
(if that cell contains Markdown or raw text).

* ## [hindcast-dayavgs-dev.ipynb](https://nbviewer.jupyter.org/github/SalishSeaCast/analysis-doug/blob/master/hindcast-dayavgs/hindcast-dayavgs-dev.ipynb)  
    
    **Development of `hindcast-dayavgs` Tool**
    
    This notebook is about initial development work on a tool to calculate
    day-averaged fields files from hour-averaged output files of SalishSeaCast hindcast runs.
    
    The motivations for this tool are:
    
    * Hindcast runs, specifically v201905, were run on the EOAS `optimum` cluster
      which suffers from significant performance degradation as the volume of run
      output increases. Because of that, the v201905 runs do not include day-averaged
      fields calculated by NEMO. But the usefulness of those fields for analysis and 
      model evaluation means that we need to produce them as a post-processing product
      so that individual researchers don't have to generate them on an *ad hoc* basis.
      
    * Timing of a selection of `ncra` commands to generate those files (see below)
      provides a baseline to compare the performance of `xarray` and `dask` to.
      `xarray` also provides more control over exclusion of unused variables/coordinates,
      and metadata buffing than `ncra`
      
    `environment.yaml` in this directory contains the conda env description for running
    this notebook, and the eventual stand-alone `hindcast_dayavgs` tool.


## License

These notebooks and files are copyright by the
[UBC EOAS MOAD Group](https://github.com/UBC-MOAD/docs/blob/master/CONTRIBUTORS.rst)
and The University of British Columbia.

They are licensed under the Apache License, Version 2.0.
http://www.apache.org/licenses/LICENSE-2.0
Please see the LICENSE file in this repository for details of the license.
