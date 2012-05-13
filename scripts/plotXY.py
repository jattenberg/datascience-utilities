#!/usr/bin/python
import sys
import numpy as np
import matplotlib.pyplot as plt
from math import log
from optparse import OptionParser

#expects a list of pairs, x, #x

parser = OptionParser(usage ="""                                                                 
Generate a plot from new-line separated numerical data of the form x,y
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

(options, args) = parser.parse_args()

 
input = open(options.filename, 'r') if options.filename else sys.stdin

xs = [] 
ys = []
for line in input:
    x, y = line.rstrip().split()
    xs.append(log(float(x)))
    ys.append(log(float(y)))


marker = options.marker if options.marker else 'r.'

plt.figure()
plt.plot(xs, ys, marker)
if options.xlabel != False:
    plt.xlabel(options.xlabel)
if options.ylabel != False:
    plt.ylabel(options.ylabel)
plt.show()
