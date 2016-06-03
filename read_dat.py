#!/usr/bin/env python
import os
import numpy as np

from features import FEATURES, GOOD_FEATURES

def read_sah_dat(filename, just_good=True):
    with open(filename, 'r') as f:
        data = [line.strip().strip('|').split('|') for line in f]
    X = np.array(data, dtype=float)
    if just_good:
        dset_name = os.path.basename(filename)[2:-4]
        good = np.array([f in GOOD_FEATURES[dset_name] for f in FEATURES[dset_name]])
        X = X[:, good]
    return X

if __name__ == '__main__':
    data = read_sah_dat('tsautocorr.dat')
    print data
