#plotXY by @jattenberg, may 2012
#
# very simple alternative to gnuplot for plotting from the command line
# able to read from a file (using the -f option) or read from a pipe


import sys
import numpy as np
import matplotlib.pyplot as plt
from math import log
from optparse import OptionParser
import pandas as pd


parser = OptionParser(usage ="""
Generate a plot from columnar numeric data. If no x value is specified, the index is used.
Usage %prog [options]                                                                                
""")
parser.add_option('-f', '--file',
                  action = 'store', dest = 'filename', default=False,
                  help="[optional] use a specified file instead of reading from stdin")
parser.add_option("-l", "--xlabel", dest='xlabel',
                  action='store', default=False,
                  help="label to use on the x axis")
parser.add_option('-y', '--ylabel',
                  action = 'store', dest = 'ylabel', default=False,
                  help="label to use on the y axis")
parser.add_option('-L', '--logscale',
                  action = 'store_true', dest = 'log_scale', default=False,
                  help="log scale values on both the x and y axis")
parser.add_option('-X', '--semilogx',
                  action = 'store_true', dest = 'semilogx', default=False,
                  help="log scale values on the x axis")
parser.add_option('-Y', '--semilogy',
                  action = 'store_true', dest = 'semilogy', default=False,
                  help="log scale values on the y axis")
parser.add_option('-s', '--subplots',
                  action = 'store_true', dest = 'subplots', default = False,
                  help = "use several subplots to represent data rather than multiple lines overlapped")
parser.add_option('-H', '--header',                                                                                                                       
                  action = 'store_true', dest = 'header', default = None,                                                                                 
                  help="treat the first row as column headers")                                                                                           
parser.add_option('-d', '--delim',                                                                                                                        
                  action='store', dest='delim', default="\t",                                                                                             
                  help="delimiter seperating columns in input")
parser.add_option('-c', '--cumulative',
                  action='store_true', dest='cum', default=False,
                  help = "store cumulative y values")
parser.add_option('-x', '--xcol', dest='xcol',
                  action='store', default=False,
                  help = "use the specified column as the x-value in the generated plot. Can be a column name or column index (from 0)")
parser.add_option('-S', '--sort',
                  action = 'store_false', dest = 'sort', default = True,
                  help = "don't sort data by the values in the x column")

(options, args) = parser.parse_args()
 
input = open(options.filename, 'r') if options.filename else sys.stdin

df = pd.read_csv(input, sep = options.delim,
                 header = 0 if options.header else None)
if options.cum:
    df = df.cumsum()

xcolumn = df.index

if options.xcol:
    if options.xcol in df.columns:
        xcolumn = df[options.xcol]
    elif options.xcol.isdigit() and int(options.xcol) < df.shape[1]:
        xcolumn = df.icol(int(options.xcol))
    else:
        raise LookupError("Unknown column: %s" % options.xcol)

ycolumns = df.drop(xcolumn.name, axis = 1) if options.xcol else df
ycolumns.index = xcolumn

if options.sort:
    ycolumns = ycolumns.sort_index()


ycolumns.plot(subplots=options.subplots,
        x = ycolumns.index,
        logx = True if options.semilogx or options.log_scale else False,
        logy = True if options.semilogy or options.log_scale else False) 

plt.legend(loc='best')

if options.ylabel != False:
    plt.ylabel(options.ylabel)
if options.xlabel != False:
    plt.xlabel(options.xlabel)

plt.show()
