Where to download DEMUD
-----------------------

https://github.com/wkiri/DEMUD

Where to get the GBT Filterbank data
------------------------------------

See the event data set prepared by Isaac Shivvers:

https://gist.github.com/stevecroft/e297e9e7dc03ca2bab616ae1e712bedf

Download `Catalog2` (the event catalog with duplicates removed)
and `DataFiles`.  Unzip the data file:

   `$ tar -zxvf KeplerGBT1.4-1.5Ghz.tgz`

This creates one subdirectory per observing row (`Row_00` to `Row_89`).  
Inside each subdirectory are several .npy files, one per detected event.

How to run on GBT Filterbank data
---------------------------------

We added a new option to DEMUD to handle GBT filterbank data saved in .npy
files.  To use it:

1. If you haven't already, create an empty `demud.config` file by running

   `$ python demud.py --make-config`

2. Specify the pathname to the GBT data in `demud.config` (look for the
GBT filterbank data set section; specify `gbtdirname` and `catalogfile`). 

3. Run

   `$ python demud.py --gbtfil`

This version seeds DEMUD with the first item in the data set.  It then
iteratively selects items that most differ from each one selected.  
By default, it runs with K=10 principal components.

Currently, the data reader only uses events with detection frequencies
within 20 MHz of 1420 MHz (see line 71 of `dataset_gbtfil.py` to modify).
This results in 18,412 observations and requires about 30 GB of RAM to process.

4. For more interesting results, try the following:

   `$ python demud.py --gbtfil --init-item=mean`: Seed DEMUD with the
   item most different from the overall data set mean.  It is likely
   more interesting than the (arbitrary) first item in the data set (default).

   `$ python demud.py --gbtfil --init-item=-1`: Seed DEMUD with the most
   unusual item in the entire data set (not the first item).  This will
   take significantly longer to start up but may yield a more interesting
   first selection.

Ideas for next steps
--------------------

* Improve (reduce) memory footprint of DEMUD for operation on large
  2D filterbank style data.
