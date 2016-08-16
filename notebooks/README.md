The IPython Notebooks in this directory are made by Doug for
sharing of Python code techniques and notes about model results analysis
code.

The links below are to static renderings of the notebooks via
[nbviewer.jupyter.org](http://nbviewer.jupyter.org/).
Descriptions below the links are from the first cell of the notebooks
(if that cell contains Markdown or raw text).

* ##[ONC-DataWebServices.ipynb](http://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-doug/raw/tip/notebooks/ONC-DataWebServices.ipynb)  
    
    **Exploring ONC Data Web Services**  
      
    Exploring the ONC data web services documented at https://wiki.oceannetworks.ca/display/help/API  

* ##[ONC-ADCP-Data.ipynb](http://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-doug/raw/tip/notebooks/ONC-ADCP-Data.ipynb)  
    
    **Exploring Getting ONC ADCP Data**  
      
    Translating the essence of `getSogAdcpData.m` from Matlab to Python  
    and from (somewhat) general purpose to pre-automation specific.  

* ##[ThalwegSalinityVideo.ipynb](http://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-doug/raw/tip/notebooks/ThalwegSalinityVideo.ipynb)  
    
    **Working Toward a Daily Updated Thalweg Salinity Contours Video**  

* ##[ONC-CTD-DataToERDDAP.ipynb](http://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-doug/raw/tip/notebooks/ONC-CTD-DataToERDDAP.ipynb)  
    
    **Development of Algorithms for ERDDAP Dataset from ONC CTD Data**  
      
    Figuring out how to transform a day's ONC CTD data from a SoG node into  
    a netCDF file that is part of an ERDDAP dataset:  
      
    * filter the ONC data to include only `qaqcFlag == 1` samples  
    * remove the `qaqcFlag` arrays as variable attributes  
    * aggregate the data into 15 minute time bins;  
    mean, variance, and count for each variable in each time bin  
    * store dataset as netCDF file  
    * generate ERDDAP `/opt/tomcat/content/erddap/datasets.xml` fragment  

* ##[NowcastFiguresRefactoring.ipynb](http://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-doug/raw/tip/notebooks/NowcastFiguresRefactoring.ipynb)  
    
    **Refactoring `nowcast.figures`**  
      
    Render figure objects returned by selected `nowcast.figures` functions.  
    Provides data from visual testing to confirm that refactoring has not  
    adversely changed figures for web pages.  
      
    Set-up and function calls should replicate as nearly as possible  
    what is done in `nowcast.workers.make_plots` worker.  

* ##[StormSurgeAlertsFeedDaily.ipynb](http://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-doug/raw/tip/notebooks/StormSurgeAlertsFeedDaily.ipynb)  
    
    **PMV Storm Surge Alert Feed Generator**  
      
    Notebook to generate `pmv.xml` feed while `nowcast.workers.make_feeds`  
    worker is in development.  

* ##[RotateGEM2.5ResearchForecastWinds.ipynb](http://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-doug/raw/tip/notebooks/RotateGEM2.5ResearchForecastWinds.ipynb)  
    
    **Rotate GEM2.5 Research Forecast Winds**  
      
    This notebook documents the process for correcting the wind direction  
    issue in the GEM2.5 research model forecast files  
    (/results/forcing/atmospheric/GEM2.5/research/).  
      


* ##[StormSurgeAlertsFeed.ipynb](http://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-doug/raw/tip/notebooks/StormSurgeAlertsFeed.ipynb)  
    
    **Storm Surge Alerts Feeds**  
      
    **Development Notes**  
      
    Notes about development of ATOM/RSS feeds for storm surge alerts.  
    Started in the process of working out the details of how to provide  
    a feed to Port Metro Vancouver during the 2015/2016 storm surge season.  
    Consideration is also given to the possibility of providing a wider collection  
    of feeds in the future.  

* ##[DFO-WaterLevelsService.ipynb](http://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-doug/raw/tip/notebooks/DFO-WaterLevelsService.ipynb)  
    
    **Getting Data from DFO Water Levels Service**  
      
    Example code to access the DFO Water Levels web service,  
    and information about what data are available there.  

* ##[SalishSeaTools_py3_issues.ipynb](http://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-doug/raw/tip/notebooks/SalishSeaTools_py3_issues.ipynb)  
    
    **Debug Python 3 Porting issues in SalishSeaTools Package**  


##License

These notebooks and files are copyright 2013-2016
by the Salish Sea MEOPAR Project Contributors
and The University of British Columbia.

They are licensed under the Apache License, Version 2.0.
http://www.apache.org/licenses/LICENSE-2.0
Please see the LICENSE file for details of the license.
