#!/usr/bin/env python
import numpy as np
import pylab as pl
from tsne import bh_sne
from sklearn.cluster import DBSCAN
from sklearn.ensemble import ExtraTreesClassifier

from read_dat import read_sah_h5

def main(datafile, normalize, ndims):
    X, features = read_sah_h5(datafile)
    Xorig = X
    if normalize:
        mean = np.average(X, axis=0)
        std = np.std(X, axis=0)
        std[np.nonzero(std == 0.0)] = 1.0 # Avoid NaNs
        X = (X - mean) / std
    np.random.seed(1)
    np.random.shuffle(X)

    X = X[::100]

    Y = bh_sne(X, d=ndims)

    dbscan = DBSCAN(eps=2.0, min_samples=5)
    C = dbscan.fit_predict(Y)

    tree = ExtraTreesClassifier(n_estimators=100)
    tree.fit(X, C)
    for f, i in zip(features, tree.feature_importances_):
        print '%s: %f' % (f, i)

    pl.scatter(Y[:, 0], Y[:, 1], color=pl.cm.spectral(C.astype(float) / np.max(C)))

    pl.show()

    print X.shape

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)

    parser.add_argument('-n', '--normalize', dest='normalize', action='store_true',
                        default=False)
    parser.add_argument('-d', '--dimensions', dest='ndims',
                        type=int, default=2)

    parser.add_argument('datafile', metavar='data-file')

    args = parser.parse_args()
    main(**vars(args))
