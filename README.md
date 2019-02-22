DATASCIENCE UTILITIES
=====================

A set of command line tools for data analysis, data mining and exploration. Most scripts are designed to work on columnar numeric data, for instance CSV data, with a configurable separator (defaulting to \t) and with an optional separator

Requirements:
=============
- Python 3.6. Other versions of python my work, but this is what I've tested with
- virtualenv
- pip


Building:
=========

Just run `./build.sh`! This builds the virtualenv and installs the library in that env.
The script also outputs several aliases that you may want to put in your shell profile for convenience. 


Some Useful Tools:
==================

+ `describe`: provides a wide variety of descriptive statistics to each column. Good for quick summary analysis.

+ reservoir_sampling: samples a specified number of rows from input, works for numeric and non-numeric data

+ `shuffle_lines`: shuffles the input data (in memory)

+ `plot_hist`: plots a histogram of values on the input columns

+ `plot_lines`: line plots of the input columns

+ `plot_hex`: Hex plots- 2D histograms on the crossproduct of input columns
