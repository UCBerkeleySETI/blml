This directory will house the DEMUD APF project.

The APF data is now working with DEMUD. The files that control how the plots and stuff look are controlled in the DEMUD respository. 

To control how the plots look, for example, with the triangles on the plots, modify the following file:
~/DEMUD/src/dataset_float_classes.py

There is a class for apf, which is a part of a superclass of all datasets. 
The APF data is in the float class since the data is floating point variables.

