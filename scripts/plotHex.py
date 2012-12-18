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
                  action = 'store', dest = 'filename', default=False)
parser.add_option('-b', '--bins', 
                  action='store', dest='bins', default=50)
parser.add_option('-d', '--delim', 
                  action='store', dest='delim', default="\t")
parser.add_option('-H', '--header', 
                  action='store_true', dest='header', default=None)
parser.add_option('-L', '--logscale',                                                                                                                                                                                                                                                                                      
                  action = 'store_true', dest = 'log_scale', default=False)

(options, args) = parser.parse_args()
 
input = open(options.filename, 'r') if options.filename else sys.stdin


df = pd.read_csv(input, sep = options.delim,
                 header = 0 if options.header else None)


#pd.tools.plotting.hist_frame(df.applymap(lambda x : log(x)) if options.log_scale else df,
#                             bins=int(options.bins))

hexbin(df[df.columns[0]].values, df[df.columns[1]].values, gridsize=20) 
xlabel(df.columns[0])
ylabel(df.columns[1])
colorbar()
show()

