Clustering Seti@Home Events
===========================

First, I convert the data to HDF5 format using the `convert_dat`
script. This is a binary format that's faster to read than plain text.

The `pairwise_dependencies` script will generate the CSV files like in
the `dependencies` directory. I used these and the `plot_dependencies`
script to make the PDF plots in the `dependencies` directory.

The `tsne_dimensionality_reduction` script does the t-SNE
dimensionality reduction (code at https://github.com/danielfrg/tsne),
DBSCAN clustering, and a random forest classifier to determine which
features are being used to separate clusters (the latter algorithm
implementations are from scikit-learn).

The `pairwise_cluster` script I tried some other clustering algorithms
(k-means, a Gaussian mixture model, and DBSCAN) on 2-dimensional data.

The `quickplot` scripts are just utilities for easily plotting
individual features or pairwise heatmaps.
