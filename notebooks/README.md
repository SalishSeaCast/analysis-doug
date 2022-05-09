The Jupyter Notebooks in this directory are made by
Doug Latornell for sharing of Python code techniques
and notes.

The links below are to static renderings of the notebooks via
[nbviewer.org](https://nbviewer.org/).
Descriptions below the links are from the first cell of the notebooks
(if that cell contains Markdown or raw text).

* ## [NowcastFiguresRefactoring.ipynb](https://nbviewer.org/github/SalishSeaCast/analysis-doug/blob/main/notebooks/NowcastFiguresRefactoring.ipynb)  
    
    **Refactoring `nowcast.figures`**
    
    Render figure objects returned by selected `nowcast.figures` functions.
    Provides data from visual testing to confirm that refactoring has not
    adversely changed figures for web pages.
    
    Set-up and function calls should replicate as nearly as possible
    what is done in `nowcast.workers.make_plots` worker.

* ## [SalishSeaCast-NEMO-ERDDAP.ipynb](https://nbviewer.org/github/SalishSeaCast/analysis-doug/blob/main/notebooks/SalishSeaCast-NEMO-ERDDAP.ipynb)  
    
    **Demonstrate Accessing SalishSeaCast NEMO Datasets from ERDDAP**
    
    This notebook is a demo of how to access results datasets from SalishSeaCast NEMO
    via the ERDDAP server.
    It uses `xarray` with the `netCDF4` backend to lazily load requested temporal/spatial
    slices for specific variables.

* ## [SalishSea2017SpillForMichael.ipynb](https://nbviewer.org/github/SalishSeaCast/analysis-doug/blob/main/notebooks/SalishSea2017SpillForMichael.ipynb)  
    
    **DFO Salish Sea 2017 Spill Exercise**
    **Surface Currents & Velocity Cross-Section**
    
    Render figure object produced by a hacked version of the 
    `nowcast.figures.research.velocity_section_and_surface` module
    for the region of interest.
    
    Set-up and function call replicates as nearly as possible what is done in the `nowcast.workers.make_plots` worker
    to help ensure that the module will work in the nowcast production context.

* ## [RotateGEM2.5ResearchForecastWinds.ipynb](https://nbviewer.org/github/SalishSeaCast/analysis-doug/blob/main/notebooks/RotateGEM2.5ResearchForecastWinds.ipynb)  
    
    **Rotate GEM2.5 Research Forecast Winds**
    
    This notebook documents the process for correcting the wind direction
    issue in the GEM2.5 research model forecast files
    (/results/forcing/atmospheric/GEM2.5/research/).
    


* ## [ONC-TWDP-nav.ipynb](https://nbviewer.org/github/SalishSeaCast/analysis-doug/blob/main/notebooks/ONC-TWDP-nav.ipynb)  
    
    **ONC scalardata API TWDP Ferry Nav Sensors Check**
    
    Explore availability of nav data from ONC scalardata API for TWDP ferry in 2016

* ## [StormSurgeAlertsFeed.ipynb](https://nbviewer.org/github/SalishSeaCast/analysis-doug/blob/main/notebooks/StormSurgeAlertsFeed.ipynb)  
    
    **Storm Surge Alerts Feeds**
    
    **Development Notes**
    
    Notes about development of ATOM/RSS feeds for storm surge alerts.
    Started in the process of working out the details of how to provide
    a feed to Port Metro Vancouver during the 2015/2016 storm surge season.
    Consideration is also given to the possibility of providing a wider collection
    of feeds in the future.

* ## [DFO-WaterLevelsService.ipynb](https://nbviewer.org/github/SalishSeaCast/analysis-doug/blob/main/notebooks/DFO-WaterLevelsService.ipynb)  
    
    **Getting Data from DFO Water Levels Service**
    
    Example code to access the DFO Water Levels web service,
    and information about what data are available there.

* ## [ONC-Ferry-DataToERDDAP.ipynb](https://nbviewer.org/github/SalishSeaCast/analysis-doug/blob/main/notebooks/ONC-Ferry-DataToERDDAP.ipynb)  
    
    **Development of Algorithms for ERDDAP Dataset from ONC Ferry Data**
    
    Figuring out how to transform a day's ONC ferry data into
    a netCDF file that is part of an ERDDAP dataset:
    
    * create a boolean mask that differentiates observations collected
    while the ferry is was on a crossing from those collected while it was
    in berth at a terminal
    * assign a crossing number to each on-crossing observation
    * filter the ONC data to include only `qaqcFlag == 1` samples
    * remove the `qaqcFlag` arrays as variable attributes
    * aggregate the data into 1 minute time bins;
    mean, variance, and count for each variable in each time bin
    * store dataset as netCDF file
    * generate ERDDAP `/opt/tomcat/content/erddap/datasets.xml` fragment

* ## [SalishSeaTools_py3_issues.ipynb](https://nbviewer.org/github/SalishSeaCast/analysis-doug/blob/main/notebooks/SalishSeaTools_py3_issues.ipynb)  
    
    **Debug Python 3 Porting issues in SalishSeaTools Package**

* ## [ThalwegSalinityVideo.ipynb](https://nbviewer.org/github/SalishSeaCast/analysis-doug/blob/main/notebooks/ThalwegSalinityVideo.ipynb)  
    
    **Working Toward a Daily Updated Thalweg Salinity Contours Video**

* ## [ONC-CTD-DataToERDDAP.ipynb](https://nbviewer.org/github/SalishSeaCast/analysis-doug/blob/main/notebooks/ONC-CTD-DataToERDDAP.ipynb)  
    
    **Development of Algorithms for ERDDAP Dataset from ONC CTD Data**
    
    Figuring out how to transform a day's ONC CTD data from a SoG node into
    a netCDF file that is part of an ERDDAP dataset:
    
    * filter the ONC data to include only `qaqcFlag == 1` samples
    * remove the `qaqcFlag` arrays as variable attributes
    * aggregate the data into 15 minute time bins;
    mean, variance, and count for each variable in each time bin
    * store dataset as netCDF file
    * generate ERDDAP `/opt/tomcat/content/erddap/datasets.xml` fragment

* ## [SalishSeaCastVizDemo.ipynb](https://nbviewer.org/github/SalishSeaCast/analysis-doug/blob/main/notebooks/SalishSeaCastVizDemo.ipynb)  
    
    **SalishSeaCast NEMO Results Visualization**
    
    Information about SalishSeaCast NEMO model results storage,
    and exploration of visualization of those results using `xarray`
    and `matplotlib`.
    
    Started during discussion of results visualization with Rachael
    on 12-Oct-2018. Narrative added later.

* ## [ONC-ADCP-Data.ipynb](https://nbviewer.org/github/SalishSeaCast/analysis-doug/blob/main/notebooks/ONC-ADCP-Data.ipynb)  
    
    **Exploring Getting ONC ADCP Data**
    
    Translating the essence of `getSogAdcpData.m` from Matlab to Python
    and from (somewhat) general purpose to pre-automation specific.

* ## [ONC-DataWebServices.ipynb](https://nbviewer.org/github/SalishSeaCast/analysis-doug/blob/main/notebooks/ONC-DataWebServices.ipynb)  
    
    **Exploring ONC Data Web Services**
    
    Exploring the ONC data web services documented at https://wiki.oceannetworks.ca/display/help/API

* ## [2ndNarrowsHADPCtoERDDAP.ipynb](https://nbviewer.org/github/SalishSeaCast/analysis-doug/blob/main/notebooks/2ndNarrowsHADPCtoERDDAP.ipynb)  
    
    **Development of Algorithms for ERDDAP Dataset from 2nd Narrows HADCP Observations**
    
    Figuring out how to transform 2nd Narrows horizontal ADCP observations from
    AIS CSV files into a netCDF file that is part of an ERDDAP dataset:
    
    * Read CSV file into `pandas` dataframe
    * Filter to include only 2nd Narrow HADCP rows
    * Convert to `xarray.Dataset`
    * Add metadata
    
    * **BONUS:** Add observations from an hourly file to an existing netCDF file
    so that we can have daily or monthly netCDF instead of hourly

* ## [CompareTwo.ipynb](https://nbviewer.org/github/SalishSeaCast/analysis-doug/blob/main/notebooks/CompareTwo.ipynb)  
    
    Susan's workhorse notebook for looking at a variety of fields at two different times.

* ## [StormSurgeAlertsFeedDaily.ipynb](https://nbviewer.org/github/SalishSeaCast/analysis-doug/blob/main/notebooks/StormSurgeAlertsFeedDaily.ipynb)  
    
    **PMV Storm Surge Alert Feed Generator**
    
    Notebook to generate `pmv.xml` feed while `nowcast.workers.make_feeds`
    worker is in development.


## License

These notebooks and files are copyright by the
[UBC EOAS MOAD Group](https://github.com/UBC-MOAD/docs/blob/master/CONTRIBUTORS.rst)
and The University of British Columbia.

They are licensed under the Apache License, Version 2.0.
http://www.apache.org/licenses/LICENSE-2.0
Please see the LICENSE file in this repository for details of the license.
