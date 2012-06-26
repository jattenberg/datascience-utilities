#plotXY by @jattenberg, may 2012
#
# very simple alternative to gnuplot for plotting from the command line
# able to read from a file (using the -f option) or read from a pipe


import sys
import numpy as np
import matplotlib.pyplot as plt
from math import log
from optparse import OptionParser

#expects a list of pairs, x, #x

parser = OptionParser(usage ="""                                                                 
Generate a plot from new-line separated numerical data of the form x,[y]
where [y] is a list of y values, each associated with the same x.
Usage %prog [options]                                                                                
""")
parser.add_option('-f', '--file',
                  action = 'store', dest = 'filename', default=False)
parser.add_option('-m', '--marker',
                  action = 'store', dest = 'marker', default=False)
parser.add_option('-x', '--xlabel',
                  action = 'store', dest = 'xlabel', default=False)
parser.add_option('-y', '--ylabel',
                  action = 'store', dest = 'ylabel', default=False)
parser.add_option('-L', '--logscale',
                  action = 'store_true', dest = 'log_scale', default=False)
parser.add_option('-X', '--semilogx',
                  action = 'store_true', dest = 'semilogx', default=False)
parser.add_option('-Y', '--semilogy',
                  action = 'store_true', dest = 'semilogy', default=False)

(options, args) = parser.parse_args()
 
input = open(options.filename, 'r') if options.filename else sys.stdin

xs = [] 
ys = []
cols = -1

for line in input:
    vals = line.rstrip().split()
    x = vals.pop(0);
    xs.append(log(float(x)) if options.log_scale or options.semilogx else float(x))
    y = [log(float(z)) if options.log_scale or options.semilogy else float(z) for z in vals]
    if cols == -1:
        cols = len(y)
    elif cols != len(y):
        raise Exception("inconsistent number of x values. have observed %d and %d" % cols, len(y)) 
    ys.append(y)

marker = options.marker if options.marker else 'r.'

plt.figure()
plt.plot(xs, ys, marker)
if options.xlabel != False:
    plt.xlabel(options.xlabel)
if options.ylabel != False:
    plt.ylabel(options.ylabel)
plt.show()
