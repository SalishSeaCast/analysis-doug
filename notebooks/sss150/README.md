The Jupyter Notebooks in this directory are made by
Doug Latornell for sharing of Python code techniques
and notes.
They are about preparation for and exploration of the results of the sss150 NEMO configuration setup in mid-2024.

The links below are to static renderings of the notebooks via
[nbviewer.org](https://nbviewer.org/).
Descriptions below the links are from the first cell of the notebooks
(if that cell contains Markdown or raw text).

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
