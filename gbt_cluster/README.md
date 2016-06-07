# GBT Cluster 
## Group 2 - Umaa, Horace, Casey and Rishi

This directory contains the jupyter notebooks written by Umaa Rebbapragada and Jasper Horrell for the BLML hackaton.  Our task was to cluster GBT filterbank data in order to find natural groupings in the data.  

# Files
* prepare_binned_data.ipynb: Prepared by Jasper.  Bins the filterbank channels from 64K down to 64
* extract_fil.ipynb: Umaa's code to read in the original .fil files and Jasper's .npy files. Extracts HOG features from Jasper's reduced images.  Plots filterbank images and HOG images side by side.  ::NOTE:: I may have introduced a bug into this notebook because it is NOT running smoothly for me anymore.  Caveat emptor.
* cluster_fil.ipynb: Performs the clustering of the HOG features using a spectral clustering algorithms.  Plots observations in each cluster
* [MISSING] Jasper's clustering results
