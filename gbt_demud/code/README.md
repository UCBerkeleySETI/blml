Where to download DEMUD
-----------------------

https://github.com/wkiri/DEMUD

How to run on GBT Spectra data
------------------------------

We added a new option to DEMUD to handle GBT spectra that are saved in 
CSV format to a text file.  To use it:

1. If you haven't already, create an empty `demud.config` file by running

   `$ python demud.py --make-config`

2. Specify the pathname to the GBT data file in `demud.config` (look for the
GBT spectra data set section). 

3. Run

   `$ python demud.py --gbt`

This version seeds DEMUD with the first item in the file.  It then
iteratively selects items that most differ from each one selected.  
By default, it runs with K=10 principal components.

4. For more interesting results, try the following:

   `$ python demud.py --gbt --init-item=-1`: Seed DEMUD with the most
   unusual item in the entire data set (not the first item).

   `$ python demud.py --gbt --init-item=-1 --variance=0.8`: DEMUD auto-selects
   the best K value needed to capture 80% of the variance in the data set.

Ideas for next steps
--------------------

* Add position features to the data set (e.g., RA and DEC), so DEMUD's
  selections will be with respect to the current pointing.

* Train DEMUD with non-A stars (less likely to have ET), 
  then apply it to select from A stars.  To do this, specify an initialization
  data set.  See `dataset_libs.py` for an example of how to add this 
  functionality to the GBTSpectra data set class.

* Use DEMUD's feature weighting capability to mask out frequencies
  with known RFI, or to tweak the relative weights of position features
  and frequency features.  See

  `$ python demud.py --featureweightmethods`

Contact: Kiri Wagstaff
