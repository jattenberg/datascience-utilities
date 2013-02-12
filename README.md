Various data analysis scripts, useful for command line data mining and exploration. Most scripts work on csv numeric data, with some configurable separator, defaulting to \t, with optional header-handling. 

Some useful examples:

describe.py: provides a wide variety of descriptive statistics to each column. Good for quick summary analysis.
reservoirSampling.py: samples rows from input, works for numeric and non-numeric data

shuffleLines.pl: shuffles the input data (in memory)

plotHist.py: plots a histogram of values on the input columns

plotLines.py: line plots of the input columns

plotHex.py: Hex plots- 2D histograms on the crossproduct of input columns


requirements:
numpy
scipy
pandas
matplotlib

only tested with python 2.7
