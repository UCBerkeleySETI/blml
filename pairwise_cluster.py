#!/usr/bin/env python
import numpy as np
import pylab as pl
from tsne import bh_sne
from sklearn.cluster import MiniBatchKMeans, DBSCAN
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.mixture import GMM
from matplotlib.colors import LogNorm
from scipy.stats import scoreatpercentile, rankdata

from read_dat import read_sah_h5

def copula_transform(xx):
    return rankdata(xx, method='ordinal')/float(xx.size)

def main(datafile, feature1, feature2, normalize, clusteroutput, percentile, copula):
    X, features = read_sah_h5(datafile, just_good=False)
    if 'id' not in features:
        ids = np.arange(len(X))
    else:
        ids = X[:, features.index('id')]
    x = X[:, features.index(feature1)]
    y = X[:, features.index(feature2)]
    D = np.column_stack([x, y])

    idx = np.random.randint(len(X), size=10000)

    D = D[idx]
    ids = ids[idx]

    if normalize:
        mean = np.average(D, axis=0)
        std = np.std(D, axis=0)
        std[np.nonzero(std == 0.0)] = 1.0 # Avoid NaNs
        Dnorm = (D - mean) / std
    elif copula:
        Dnorm = np.column_stack([copula_transform(f) for f in D.T])
    else:
        Dnorm = D

    kmeans = MiniBatchKMeans(n_clusters=50)
    gmm = GMM(n_components=200, covariance_type='full', verbose=True)
    #C = gmm.fit_predict(Dnorm)
    dbscan = DBSCAN(eps=100.0, min_samples=1)
    C = dbscan.fit_predict(Dnorm)
    print C

    with open(clusteroutput, 'w+') as f:
        for c, i in zip(C, ids):
            f.write('%d,%d\n' % (i, c))

    pl.scatter(D[:, 0], D[:, 1], color=pl.cm.spectral(C.astype(float) / np.max(C)))

#    for c in np.unique(C):
#        pl.bar(0, 0, lw=0, ec='none',
#            fc=pl.cm.spectral(float(c) / np.max(C)), label='Cluster %d' % c)
#    pl.legend(loc='upper left')

    if percentile > 0:
        pl.xlim(
            scoreatpercentile(x, percentile),
            scoreatpercentile(x, 100-percentile)
        )
        pl.ylim(
            scoreatpercentile(y, percentile),
            scoreatpercentile(y, 100-percentile)
        )

    pl.xlabel(feature1)
    pl.ylabel(feature2)
    pl.show()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)

    parser.add_argument('datafile')
    parser.add_argument('feature1')
    parser.add_argument('feature2')
    parser.add_argument('-n', '--normalize', action='store_true',
                        default=False)
    parser.add_argument('-p', '--percentile', type=float, default=0)
    parser.add_argument('-c', '--copula', default=False, action='store_true')
    parser.add_argument('clusteroutput')

    args = parser.parse_args()
    main(**vars(args))
