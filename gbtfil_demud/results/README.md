DEMUD results on GBT filterbank data
------------------------------------

This directory contains a visualization of the first 10 selections of
interesting items made by DEMUD when analyzing GBT filterbank data.
In this experiment, all events (SNR > 10.0) with a center frequency
within 20 MHz of 1420 MHz were analyzed (a total of 18,412 events).
Each one was represented by a 100x100 (time, frequency) cropped region 
from the original filterbank data.

Each plot contains:

* Top row: original filterbank data and reconstructed data using the 
  current DEMUD model.

* Bottom row: residual plot showing where the original (observed) data
  is brighter than (red colors) or darker than (blue colors) DEMUD's 
  reconstruction.  This allows us to interpret the selection; pixels with
  large magnitudes (high or low) explain why DEMUD chose that item.

DEMUD's model is updated after each selection, so it builds a richer
understanding of variety in the data set as it progresses.

The directory also contains a text file called `demud.log` that contains
the output of the DEMUD run with timing and additional details for
each selection.

Contact: Kiri Wagstaff
