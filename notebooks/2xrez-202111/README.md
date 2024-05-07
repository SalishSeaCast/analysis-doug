The Jupyter Notebooks in this directory are made by
Doug Latornell for sharing of Python code techniques
and notes.
They are about preparation for and exploration of the results of the SalishSeaCast v202111 double resolution experiment in mid-2024.

The links below are to static renderings of the notebooks via
[nbviewer.org](https://nbviewer.org/).
Descriptions below the links are from the first cell of the notebooks
(if that cell contains Markdown or raw text).

* ## [coordinates.ipynb](https://nbviewer.org/github/SalishSeaCast/analysis-doug/blob/main/notebooks/2xrez-202111/coordinates.ipynb)  
    
    **Coordinates**
    
    Explore the coordinates file for the double resolution run:
    * look at the coordinates file that Susan created for the 2022 experiment
    * check the coordinates in the lower Fraser River are re: Michael's grid refinements there
    * investigate adding coordinate rows at the south edge of the domain to fully include the south
      coastline of Puget Sound and add a sufficient land buffer for OceanParcels to work correctly in 
      that area re: Jose's findings about particle losses at water boundaries
    
    Construct new 202405 coordinates file for future SalishSeaCast hindcast/production:
    * add coordinate rows at the south edge of the domain to fully include the south
      coastline of Puget Sound and add a sufficient land buffer for OceanParcels to work correctly
    * add meta data to variables guided by
      https://salishsea.eos.ubc.ca/erddap/info/ubcSSn2DMeshMaskV21-08/index.html
    * add notes to https://github.com/SalishSeaCast/grid/blob/main/README.rst to document at least some
      of the files in the `grid` repository
    
    
    Transform 202405 coordinates file to double resolution for the 2024 experiment:
    * follow Susan's process in
      https://github.com/SalishSeaCast/tools/blob/main/double_resolution/coordinates.ipynb


## License

These notebooks and files are copyright by the
[UBC EOAS MOAD Group](https://github.com/UBC-MOAD/docs/blob/main/CONTRIBUTORS.rst)
and The University of British Columbia.

They are licensed under the Apache License, Version 2.0.
https://www.apache.org/licenses/LICENSE-2.0
Please see the LICENSE file in this repository for details of the license.
