DATASCIENCE UTILITIES
=====================

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/jattenberg/atomic-design-ui/blob/master/LICENSEs)
[![HitCount](http://hits.dwyl.com/jattenberg/datascience-utilities.svg)](http://hits.dwyl.com/jattenberg/datascience-utilities)
[![PyPI version](https://badge.fury.io/py/datascience-utilities.svg)](https://badge.fury.io/py/datascience-utilities)


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

+ `ztest`: perform the z-test

+ `normal`: draw from a normal distribution

+ `exponential`: draw from an exponential distribution

+ `poisson`: draw from a poisson distribution

+ `column_selector`: slightly more powerful version of cut

Examples:
=========

`normal | shuffle_lines | reservoir_sample -n 5`

`normal -D 2 | plot_hex`

`paste <(perl -e  'for ($i = 0; $i < 10000; $i ++) { print rand(), "\t", ('a'..'z')[int(rand()*26)], "\t", 50*rand(), "\n" } ') <(normal -n 10000) | describe`

`perl -e  'BEGIN{print "SHOES\tGLASSES\n"} for ($i = 0; $i < 100; $i ++) { print rand(), "\t", 50*rand(), "\n" } ' | plot_xy -O -H`

`paste <(normal -m 5 -s 20 -n 10000) <(perl -e 'foreach (1..10000) { print rand(), "\n"}' ) | plot_hex`

`paste <(normal -m 5 -s 20 -n 10000) <(perl -e 'foreach (1..10000) { print rand(), "\n"}' ) <(exponential -n 10000) <(poisson -n 10000 -l 1) | describe`

`paste <(normal -m 5 -s 20 -n 10000) <(perl -e 'foreach (1..10000) { print rand(), "\n"}' ) | csv_to_json -L | json_to_csv -L -i`

`paste <(poisson -n 10000) <(normal -m 5 -s 20 -n 10000) <(perl -e 'foreach (1..10000) { print rand(), "\n"}' ) | csv_to_json -L | json_to_csv -L -i | column_selector -C 0,1 -H`

`paste <(perl -le 'foreach (1..50){ $r = rand(); $x = (-2.0*log(($r < 0.5) ? $r : 1 - $r))**0.5;  $o = $x - ((0.010328*$x + 0.802853)*$x + 2.515517)/(((0.001308*$x + 0.189269)*$x + 1.432788)*$x + 1.0); print (($r < 0.5) ? $o : -$o)}') <(perl -le 'foreach (1..50){ print rand() }') | plot_xy`
