#!/usr/bin/env python
import numpy as np
from itertools import combinations
from progressbar import ProgressBar, ETA, Bar

from read_dat import read_sah_h5
from rdc import rdc

def main(datafile, outputfile):
    X, features = read_sah_h5(datafile, just_good=False)

    result = []
    progress = ProgressBar(widgets=['Computing dependencies: ', Bar('='), ETA()])
    for f1, f2 in progress(list(combinations(features, 2))):
        x = X[:, features.index(f1)]
        y = X[:, features.index(f2)]
        result.append('%s,%s,%f' % (f1, f2, rdc(x, y, n=5)))

    with open(outputfile, 'w+') as f:
        f.write('\n'.join(result))

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)

    parser.add_argument('datafile')
    parser.add_argument('outputfile')

    args = parser.parse_args()
    main(**vars(args))
