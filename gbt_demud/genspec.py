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
	onedspec = rebin(fil.data,277,1)[0]
	print onedspec
	allspec.append(onedspec)

# frequencies (from the last filterbank file)
freqs = fil.freqs
allspecnp = np.asarray(allspec)
print allspecnp
np.save("allspec.npy",allspecnp)
ascii.write(allspecnp, 'values.dat', names=freqs,format='csv')
# display the "superwaterfall"
#imshow(allspecnp,aspect='auto',vmin=0,vmax=5e10,extent=[1501.466,1688.963,0,89])
