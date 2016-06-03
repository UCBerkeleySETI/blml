#!/usr/bin/env python
import numpy as np
import pylab as pl
from matplotlib.patches import Rectangle
from tsne import bh_sne
from sklearn.cluster import DBSCAN
from sklearn.ensemble import ExtraTreesClassifier
from scipy.stats import rankdata

from read_dat import read_sah_h5

def copula_transform(xx):
    return rankdata(xx, method='ordinal')/float(xx.size)

def main(datafile, normalize, ndims, copula, clusteroutput, subsample):
    X, features = read_sah_h5(datafile)
    I, _ = read_sah_h5(datafile, just_good=False)
    ids = I[:, 0]

    Xorig = X
    if normalize:
        mean = np.average(X, axis=0)
        std = np.std(X, axis=0)
        std[np.nonzero(std == 0.0)] = 1.0 # Avoid NaNs
        X = (X - mean) / std

    idx = np.random.randint(len(X), size=subsample)

    X = X[idx]
    ids = ids[idx]

    if copula:
        X = np.column_stack([copula_transform(x) for x in X.T])

    Y = bh_sne(X, d=ndims)

    dbscan = DBSCAN(eps=1.75, min_samples=5)
    C = dbscan.fit_predict(Y)

    tree = ExtraTreesClassifier(n_estimators=100)
    tree.fit(X, C)
    for f, i in zip(features, tree.feature_importances_):
        print '%s: %f' % (f, i)

    with open(clusteroutput, 'w+') as f:
        for c, i in zip(C, ids):
            f.write('%d,%d\n' % (i, c))

    pl.scatter(Y[:, 0], Y[:, 1], color=pl.cm.spectral(C.astype(float) / np.max(C)))

    for c in np.unique(C):
        pl.bar(0, 0, lw=0, ec='none', fc=pl.cm.spectral(float(c) / np.max(C)), label='Cluster %d' % c)
    pl.legend()

    pl.show()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)

    parser.add_argument('-n', '--normalize', action='store_true',
                        default=False)
    parser.add_argument('-c', '--copula', action='store_true', default=False)
    parser.add_argument('-d', '--dimensions', dest='ndims',
                        type=int, default=2)
    parser.add_argument('-s', '--subsample', type=int, default=4000)

    parser.add_argument('datafile')
    parser.add_argument('clusteroutput')

    args = parser.parse_args()
    main(**vars(args))
