This folder will house the code used in the APF-DEMUD project.

Where to download DEMUD
-----------------------

https://github.com/wkiri/DEMUD

We added a new option to DEMUD to handle APF spectra that are saved in 
CSV format to a text file.  To use it:

0. If you haven't already, create an empty `demud.config` file by running

   `$ python demud.py --make-config`

1. Specify the pathname to the APF data file in `demud.config` (look for the
APF spectra data set section). 

2. Run

   `$ python demud.py -b`