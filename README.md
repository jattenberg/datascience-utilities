DATASCIENCE UTILITIES
=====================

[![Travis CI w/ Logo](https://img.shields.io/travis/jattenberg/datascience-utilities/master.svg?logo=travis)](https://travis-ci.org/jattenberg/datascience-utilities)  
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/jattenberg/atomic-design-ui/blob/master/LICENSEs)
[![HitCount](http://hits.dwyl.io/jattenberg/datascience-utilities.svg)](http://hits.dwyl.io/jattenberg/datascience-utilities)
[![PyPi Version](https://img.shields.io/pypi/v/jattenberg.svg)](https://pypi.python.org/pypi/datascience-utilities/)


A set of command line tools for data analysis, data mining and exploration. Most scripts are designed to work on columnar numeric data, for instance CSV data, with a configurable separator (defaulting to \t) and with an optional separator

Requirements:
=============
- Python 3.6. Other versions of python my work, but this is what I've tested with
- pipx / pip


Building:
=========

Just run `./build.sh`! This installs `pipx` if it's not installed using pip and uses `pipx`
to build the library in a virtual env, putting that on your path. by default, this is at
`~/.local/bin`, which may not be on your path, `pipx` tries to add it. 

The `build.sh` script also accepts an optional parameter "iterm" to facilitate inline plotting in iterm2


Some Useful Tools:
==================

+ `describe`: provides a wide variety of descriptive statistics to each column. Good for quick summary analysis.

+ `reservoir_sampling`: samples a specified number of rows from input, works for numeric and non-numeric data

+ `shuffle_lines`: shuffles the input data (in memory)

+ `plot_hist`: plots a histogram of values on the input columns

+ `plot_lines`: line plots of the input columns

+ `plot_hex`: Hex plots- 2D histograms on the crossproduct of input columns

+ `json_to_csv`: convert json data to csv with various options

+ `csv_to_json`: convert csv data to json with various options


Examples:
=========

`normal | shuffle_lines | reservoir_sample -n 5`

`normal -D 2 | plot_hex`

`paste <(perl -e  'for ($i = 0; $i < 10000; $i ++) { print rand(), "\t", ('a'..'z')[int(rand()*26)], "\t", 50*rand(), "\n" } ') <(normal -n 10000) | describe`

`perl -e  'BEGIN{print "SHOES\tGLASSES\n"} for ($i = 0; $i < 100; $i ++) { print rand(), "\t", 50*rand(), "\n" } ' | plot_xy -O -H`

`paste <(normal -m 5 -s 20 -n 10000) <(perl -e 'foreach (1..10000) { print rand(), "\n"}' ) | plot_hex`

`paste <(normal -m 5 -s 20 -n 10000) <(perl -e 'foreach (1..10000) { print rand(), "\n"}' ) <(exponential -n 10000) <(poisson -n 10000 -l 1) | describe`

`paste <(normal -m 5 -s 20 -n 10000) <(perl -e 'foreach (1..10000) { print rand(), "\n"}' ) | csv_to_json -L | json_to_csv -L -i`