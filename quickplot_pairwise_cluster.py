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

def main(datafile, feature1, feature2, clusterfile, clusterid,
         bins, percentile, copula, logscale):
    X, features = read_sah_h5(datafile, just_good=False)
    x = X[:, features.index(feature1)]
    y = X[:, features.index(feature2)]
    ids = X[:, features.index('id')]

    include = {}
    with open(clusterfile, 'r') as f:
        for line in f:
            i, c = map(float, line.strip().split(','))
            include[i] = (c == clusterid)

    include_mask = np.array([include.get(i, False) for i in ids])
    x = x[include_mask]
    y = y[include_mask]

    if percentile > 0 and not copula:
        bx = np.linspace(
            scoreatpercentile(x, percentile),
            scoreatpercentile(x, 100-percentile),
            bins)
        by = np.linspace(
            scoreatpercentile(y, percentile),
            scoreatpercentile(y, 100-percentile),
            bins)
        bins = (bx, by)

    if copula:
        x = copula_transform(x)
        y = copula_transform(y)

    if logscale:
        pl.hist2d(x, y, bins=bins, norm=LogNorm())
    else:
        pl.hist2d(x, y, bins=bins)
    pl.xlabel(feature1)
    pl.ylabel(feature2)
    pl.colorbar()
    pl.show()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)

    parser.add_argument('datafile')
    parser.add_argument('feature1')
    parser.add_argument('feature2')
    parser.add_argument('clusterfile')
    parser.add_argument('clusterid', type=int)
    parser.add_argument('-b', '--bins', type=int, default=100)
    parser.add_argument('-p', '--percentile', type=float, default=0)
    parser.add_argument('-c', '--copula', default=False, action='store_true')
    parser.add_argument('-l', '--logscale', default=False, action='store_true')

    args = parser.parse_args()
    main(**vars(args))
