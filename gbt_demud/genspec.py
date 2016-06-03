#!/usr/bin/env/python

# Collapse GBT filterbank files in time
# Display input 1D spectra
# Write out to CSV for intput into DEMUD
# S. Croft 2016 Jun 3

import sys
import glob
import numpy as np
import re
from filterbank import *
from astropy.io import ascii

# array to hold all output spectra
allspec = []
allspecdata = []

# find all filterbank files in the current directory
for fname in glob.glob("*.fil"):
#	print fname
# look for HIPparcos stars
	m = re.search (r'HIP\d+_\d+',fname)
	if m:
		starname = m.group(0)
	else:
		starname = "UNKNOWN"
	print starname
# read in the filterbank file
	fil = Filterbank(fname)
#	print fil.data.shape
# average over 277 time samples, resulting in a 1D spectrum
	dataline = [starname]
	onedspec = rebin(fil.data,277,1)[0]
# csv file lines start with the star name
	dataline.extend(onedspec)
#	print onedspec
	allspec.append(onedspec)
	allspecdata.append(dataline)


# frequencies (from the last filterbank file)
freqs = fil.freqs
# csv file starts with a comment - need to manually edit output to remove the first comma after the hash
freqsdata = ['#']
freqsdata.extend(freqs)
allspecnp = np.asarray(allspec)
allspecdatanp = np.asarray(allspecdata)
print allspecnp
np.save("allspec.npy",allspecnp)
ascii.write(allspecdatanp, 'genspec.csv', names=freqsdata,format='csv')
# display the "superwaterfall"
#imshow(allspecnp,aspect='auto',vmin=0,vmax=5e10,extent=[1501.466,1688.963,0,89])
