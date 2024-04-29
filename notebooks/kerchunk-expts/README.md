The Jupyter Notebooks in this directory are made by
Doug Latornell for sharing of Python code techniques
and notes.

The links below are to static renderings of the notebooks via
[nbviewer.org](https://nbviewer.org/).
Descriptions below the links are from the first cell of the notebooks
(if that cell contains Markdown or raw text).

* ## [mulit_file_kerchunk.ipynb](https://nbviewer.org/github/SalishSeaCast/analysis-doug/blob/main/notebooks/kerchunk-expts/mulit_file_kerchunk.ipynb)  
    
    **Multi-file Kerchunk Dataset for SalishSeaCast netCDF Results**
    
    Scan a collection of SalishSeaCast netCDF files to create a collection of Kerchunk reference files.
    Then combine those references to create a combine reference for a virtual dataset for the collection.
    Finally,
    demonstrate access to an arbitrary slice in the collection.
    This notebook is guided by the Multi-File Datasets with Kerchunk notebook in Project Pythia Kerchunk Cookbook.
    
    ref: https://zenodo.org/badge/latestdoi/588661659

* ## [single_file_kerchunk.ipynb](https://nbviewer.org/github/SalishSeaCast/analysis-doug/blob/main/notebooks/kerchunk-expts/single_file_kerchunk.ipynb)  
    
    **Kerchunk a Single SalishSeaCast netCDF File**
    
    Scan a single SalishSeaCast netCDF file to create a Kerchunk virtual dataset and use the dataset
    in `xarray` via `fsspec`. This notebook is guided by the Kerchunk Basics notebook in Project Pythia
    Kerchunk Cookbook.
    
    ref: https://zenodo.org/badge/latestdoi/588661659

* ## [15may_physics_json_kerchunk.ipynb](https://nbviewer.org/github/SalishSeaCast/analysis-doug/blob/main/notebooks/kerchunk-expts/15may_physics_json_kerchunk.ipynb)  
    
    **SaliishSeaCast 15may Kerchunk with .json References**
    
    Scan a collection of SalishSeaCast netCDF files to create a collection of Kerchunk reference files.
    Then combine those references to create a combine reference for a virtual dataset for the collection.
    Finally,
    demonstrate access to an arbitrary slice in the collection.
    This notebook is guided by the Store Kerchunk Reference Files as Parquet notebook in Project Pythia Kerchunk Cookbook.
    
    ref: https://zenodo.org/badge/latestdoi/588661659

* ## [parquet_kerchunk.ipynb](https://nbviewer.org/github/SalishSeaCast/analysis-doug/blob/main/notebooks/kerchunk-expts/parquet_kerchunk.ipynb)  
    
    **Parquet Storage for Multi-file Kerchunk Reference Dataset**
    
    Scan a collection of SalishSeaCast netCDF files to create a collection of Kerchunk reference dicts
    in memory.
    Then combine those references to create a combined reference for a virtual dataset for the collection
    stored as a `Parquet` storage instead of `json`.
    `Parquet` should make the combined reference storage smaller and its use to access the netCDF dataset
    files use less memory.
    Finally,
    demonstrate access to an arbitrary slice in the collection.
    This notebook is guided by the Store Kerchunk Reference Files as Parquet notebook in Project Pythia Kerchunk Cookbook.
    
    ref: https://zenodo.org/badge/latestdoi/588661659


## License

These notebooks and files are copyright by the
[UBC EOAS MOAD Group](https://github.com/UBC-MOAD/docs/blob/main/CONTRIBUTORS.rst)
and The University of British Columbia.

They are licensed under the Apache License, Version 2.0.
https://www.apache.org/licenses/LICENSE-2.0
Please see the LICENSE file in this repository for details of the license.
