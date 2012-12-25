#plotHist by @jattenberg, Dec 2012
#reads 2 columns as floating point values in a file or a unix pipe
#builds a hex plot first 2

import sys
from math import log
import pandas as pd
from optparse import OptionParser
from matplotlib.pyplot import *





parser = OptionParser(usage ="""                                                                 
Generate a hexplot from new-line separated numerical data of the form x1, x2
each column containing values that are to be compared in the hexplot
Usage %prog [options]                                                                                
""")
parser.add_option('-f', '--file',
                  action = 'store', dest = 'filename', default=False,
                  help="[optional] use a specified file instead of reading from stdin")
parser.add_option('-b', '--bins', 
                  action='store', dest='bins', default=20,
                  help="number of bins in histogram (default 20)")
parser.add_option('-d', '--delim', 
                  action='store', dest='delim', default="\t")
parser.add_option('-H', '--header', 
                  action='store_true', dest='header', default=None,
                  help="treat the first row as column headers")
parser.add_option('-L', '--logscale',                                                                                                                                                                                                                                                                                      
                  action = 'store_true', dest = 'log_scale', default=False,
                  help="use log values when for constructing histogram")
parser.add_option('-x', '--xval',
                 action = 'store', dest = 'x', default = "0",
                 help = "column used for the x axis")
parser.add_option('-y', '--yval',
                 action = 'store', dest = 'y', default = "1",
                 help = "column used for the y axis")


(options, args) = parser.parse_args()
 
input = open(options.filename, 'r') if options.filename else sys.stdin


df = pd.read_csv(input, sep = options.delim,
                 header = 0 if options.header else None)



if options.x in df.columns:
    x = df[options.x]
elif options.x.isdigit() and int(options.x) < df.shape[1]:
    x = df.icol(int(options.x))
else:
    raise LookupError("Unknown X column: %s" % options.x)

if options.y in df.columns:
    y = df[options.y]
elif options.x.isdigit()  and int(options.y) < df.shape[1]:
    y = df.icol(int(options.y))
else:
    raise LookupError("Unknown X column: %s" % options.x)


hexbin(x.values, y.values,
       gridsize=int(options.bins),
       bins="log" if options.log_scale else None) 
xlabel(x.name)
ylabel(y.name)
colorbar()
show()

