Where to download DEMUD
-----------------------

https://github.com/wkiri/DEMUD

We added a new option to DEMUD to handle APF spectra that are saved in 
CSV format to a text file.  To use it:

1. If you haven't already, create an empty `demud.config` file by running

   `$ python demud.py --make-config`

2. Specify the pathname to the APF data file in `demud.config` (look for the
APF spectra data set section). 

3. Run

   `$ python demud.py -b`

This version seeds DEMUD with the first item in the file.  It then
iteratively selects items that most differ from each one selected.  
By default, it runs with K=2 principal components.

4. For more interesting results, try the following:

   `$ python demud.py -b --init-item=-1`: Seed DEMUD with the most
   unusual item in the entire data set (not the first item).

   `$ python demud.py -b --init-item=-1 --variance=0.8`: DEMUD auto-selects
   the best K value needed to capture 80% of the variance in the data set.
