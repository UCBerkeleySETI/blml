#!/usr/bin/env python
import numpy as np
import pylab as pl
from tsne import bh_sne
from sklearn.cluster import DBSCAN
from sklearn.ensemble import ExtraTreesClassifier
from matplotlib.colors import LogNorm
from scipy.stats import scoreatpercentile, rankdata

from read_dat import read_sah_h5

def copula_transform(xx):
    return rankdata(xx, method='ordinal')/float(xx.size)

def main(datafile, feature1, bins, percentile, logscale):
    X, features = read_sah_h5(datafile, just_good=False)
    x = X[:, features.index(feature1)]

    if percentile > 0:
        bins = np.linspace(
            scoreatpercentile(x, percentile),
            scoreatpercentile(x, 100-percentile),
            bins)

    pl.hist(x, bins=bins, histtype='step', color='k')

    if logscale:
        pl.set_yscale('log')
    pl.xlabel(feature1)
    pl.show()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)

    parser.add_argument('datafile')
    parser.add_argument('feature1')
    parser.add_argument('-b', '--bins', type=int, default=100)
    parser.add_argument('-p', '--percentile', type=float, default=0)
    parser.add_argument('-l', '--logscale', default=False, action='store_true')

    args = parser.parse_args()
    main(**vars(args))
