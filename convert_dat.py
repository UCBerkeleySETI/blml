#!/usr/bin/env python
import numpy as np
import h5py
from contextlib import closing

from read_dat import read_sah_dat, get_features
from features import FEATURES

def main(datafile, outputfile):
    data = read_sah_dat(datafile, just_good=False)
    features = get_features(datafile)
    with closing(h5py.File(outputfile, 'w')) as l2:
        l2['features'] = np.array(features)
        l2['data'] = data

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    parser.add_argument('datafile')
    parser.add_argument('outputfile')

    args = parser.parse_args()
    main(**vars(args))
