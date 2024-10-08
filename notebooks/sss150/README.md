The Jupyter Notebooks in this directory are made by
Doug Latornell for sharing of Python code techniques
and notes.
They are about preparation for and exploration of the results of the sss150 NEMO configuration setup in mid-2024.

The links below are to static renderings of the notebooks via
[nbviewer.org](https://nbviewer.org/).
Descriptions below the links are from the first cell of the notebooks
(if that cell contains Markdown or raw text).

* ## [NoSnow.ipynb](https://nbviewer.org/github/SalishSeaCast/analysis-doug/blob/main/notebooks/sss150/NoSnow.ipynb)  
    
    **Create `no_snow.nc` File for `sss150` Domain**
    
    Create a netCDF4 file containing 1 variable named `snow`.
    The coordinates of the variable are `y` and `x` and their sizes are 826 and 710.
    The value of `snow` at all points in the domain is floating point zero.
    
    The resulting `no_snow.nc` file can be used as an annual climatology in NEMO atmospheric forcing
    that does not require on-the-fly interpolation.
    It imposes a no snow, ever condition on the `sss150` NEMO configuration.

* ## [xios2_update-check.ipynb](https://nbviewer.org/github/SalishSeaCast/analysis-doug/blob/main/notebooks/sss150/xios2_update-check.ipynb)  
    
    **Check Results of Runs with Updated XIOS-2**
    
    Compare results of SalishSeaCast_Blue runs with XIOS-2 updated to successfully build with GCC-9 compilers against pre-update results.
    
    The update of `salish` to Ubuntu 20.04.2 LTS us to change from GCC-5 compilers and OpenMPI-2 library to GCC-9 and OpenMPI-4.
    Builds of NEMO configurations using XIOS-2 at svn r1660 that we have been using since Apr-2019 fail when compiled with GCC-9 due to
    memory allocation errors or runaway memory consumption.
    Updating XIOS-2 to the upstream trunk in Sep/Oct-2024 resulted in builds that produced successful test runs.
    Initial testing was done using svn r2659.
    The revision pushed to our XIOS-2 repository on GitHub was svn r2660.  

* ## [add_sshbdyPR-check.ipynb](https://nbviewer.org/github/SalishSeaCast/analysis-doug/blob/main/notebooks/sss150/add_sshbdyPR-check.ipynb)  
    
    **Check Michael's `add_sshbdy` Pull Request**
    
    Compare results of a SalishSeaCast (green) run on `salish` to one built from
    [Michael's `add_sshbdy` Pull Request](https://github.com/SalishSeaCast/NEMO-3.6-code/pull/6)
    to confirm that the PR code is isolated so that we can merge the PR without affecting runs
    that use the `PROD-nowcast-green-202111` tagged SalishSeaCast configuration.
    The PR adds code to provide the option of imposing sea surface height at boundaries.
    Susan's explanation of the PR:
    > The new boundary conditions that Michael added are needed because the boundary between SalishSeaCast and SSS150 is handled differently than the boundaries of SalishSeaCast. 
    > SalishSeaCast uses Flather boundary conditions to add a SSH from Neah Bay and gets two-dimensional velocities from the Flather Scheme.
    > SalishSeaCast has separate tidal forcing.  SSS150 uses SSH and barotropic velocities to force the 2-D (barotropic) circulation including both tides and longer period SSH variations.


## License

These notebooks and files are copyright by the
[UBC EOAS MOAD Group](https://github.com/UBC-MOAD/docs/blob/main/CONTRIBUTORS.rst)
and The University of British Columbia.

They are licensed under the Apache License, Version 2.0.
https://www.apache.org/licenses/LICENSE-2.0
Please see the LICENSE file in this repository for details of the license.
