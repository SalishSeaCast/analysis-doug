The IPython Notebooks in this directory are made by Doug for
sharing of Python code techniques and notes about model results analysis
code regarding the integration of the Strait of Georgia WaveWatchIII®
model with the SalishSeaNowcast system.

The links below are to static renderings of the notebooks via
[nbviewer.jupyter.org](https://nbviewer.jupyter.org/).
Descriptions below the links are from the first cell of the notebooks
(if that cell contains Markdown or raw text).

* ##[ExploreWW3Results.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-doug/raw/tip/notebooks/SoG-waves/ExploreWW3Results.ipynb)  
    
    **Exploration of WWatch3 Results**  
      
    Basic exploration and visualization of wwatch3 fields and points results files from   
    Salish Sea Nowcast system SoG-waves run.  

* ##[12Apr17Forecast.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-doug/raw/tip/notebooks/SoG-waves/12Apr17Forecast.ipynb)  
    
    **Exploration of WWatch3 Results for 12Apr17 Forecast Run**  
      
    Basic exploration and visualization of wwatch3 fields and points results files from   
    Salish Sea Nowcast system SoG-waves run.  
      
    From 12-Apr-2017 forecast run initiated with   
    quiescent initial wave state on 11-Apr-2017,  
    and forced with hourly HRDPS winds and Salish Sea NEMO nowcast/forecast currents.  

* ##[GridAngles.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-doug/raw/tip/notebooks/SoG-waves/GridAngles.ipynb)  
    
    **Investigate Orientation Wind and Currents Grids for WaveWatch**  
      
    ww3 requires wind and currents forcing files to be on a   
    "spherical lat-long grid, with constant dlon, dlat"  
    (maybe the same as a [plate carrée](https://en.wikipedia.org/wiki/Equirectangular_projection)  
    grid?).  
    This notebook examines the Salish Sea NEMO atmospheric forcing files like  
      
    `/results/forcing/atmospheric/GEM2.5/operational/ops_y2017m03d17.nc`  
      
    and the `u` and `v` current component output files like  
      
    `/results/SalishSea/nowcast-blue/17mar17/SalishSea_1h_20170317_20170317_grid_U.nc`  
      
    and  
      
    `/results/SalishSea/nowcast-blue/17mar17/SalishSea_1h_20170317_20170317_grid_V.nc`  
      
    and their associated mesh mask file:  
      
    `NEMO-forcing/grid/mesh_mask_downbyone2.nc`  
      
    or the  
      
    https://salishsea.eos.ubc.ca/erddap/info/ubcSSn2DMeshMask2V16-07/index.html  
      
    ERDDAP dataset,  
    to determine what transformation of them is required to produce input wind and current files  
    for ww3.  
      
    The mesh mask file is required because the latitudes and longitudes of the velocity grid points  
    are not stored in the `*grid_Ū.nc` and `*grid_V.nc` files.  


##License

These notebooks and files are copyright 2013-2017
by the Salish Sea MEOPAR Project Contributors
and The University of British Columbia.

They are licensed under the Apache License, Version 2.0.
http://www.apache.org/licenses/LICENSE-2.0
Please see the LICENSE file for details of the license.
