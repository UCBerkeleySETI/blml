#!/usr/bin/env python
import os
import numpy as np
import h5py
from contextlib import closing

from features import FEATURES, GOOD_FEATURES, STRIP_BINARY

def get_features(filename):
    dset_name = os.path.basename(filename)[2:].split('.')[0]
    return FEATURES[dset_name]

def read_sah_dat(filename, just_good=True):
    dset_name = os.path.basename(filename)[2:].split('.')[0]
    with open(filename, 'r') as f:
        if STRIP_BINARY[dset_name]:
            data = [line.strip().strip('|').split('|')[:-1] for line in f]
        else:
            data = [line.strip().strip('|').split('|') for line in f]
    X = np.array(data, dtype=float)
    if just_good:
        good = np.array([f in GOOD_FEATURES[dset_name] for f in FEATURES[dset_name]])
        X = X[:, good]
    return X

def read_sah_h5(filename, just_good=True):
    with closing(h5py.File(filename, 'r')) as f:
        data = np.array(f['data'])
        features = list(f['features'])
    index = dict([(f, i) for i, f in enumerate(features)])
    if just_good:
        dset_name = os.path.basename(filename)[2:].split('.')[0]
        features = list(GOOD_FEATURES[dset_name])
        data = np.column_stack([data[:, index[f]] for f in features])
    return data, features

if __name__ == '__main__':
    data = read_sah_dat('tsautocorr.dat')
    print data
