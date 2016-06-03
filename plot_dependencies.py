#!/usr/bin/env python
import os
import pylab as pl
import numpy as np
import pydot

from features import GOOD_FEATURES

def main(depfile, outputfile, threshold):
    dset_name = os.path.basename(depfile)[2:].split('.')[0]
    good = GOOD_FEATURES[dset_name]
    good = list(good) + ['time', 'ra', 'dec']

    dot = pydot.Dot(graph_type='graph')
    with open(depfile, 'r') as f:
        for line in f:
            f1, f2, d = line.strip().split(',')
            if (f1 in good) and (f2 in good):
                d = float(d)
                if d > threshold:
                    dot.add_edge(pydot.Edge(f1, f2, label='%.3f' % d))
                    print '%s %s %f' % (f1, f2, float(d))

    for g in good:
        dot.add_node(pydot.Node(g))

    dot.write_pdf(outputfile)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)

    parser.add_argument('depfile')
    parser.add_argument('outputfile')
    parser.add_argument('-t', '--threshold', type=float, default=0.2)

    args = parser.parse_args()
    main(**vars(args))
