#plotHist by @jattenberg, Dec 2012
#reads 2 columns as floating point values in a file or a unix pipe
#builds a hex plot first 2
"""
Copyright (c) 2013 Josh Attenberg

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import sys
from math import log
import pandas as pd
from optparse import OptionParser
from matplotlib.pyplot import *
import seaborn as sns


def get_parser():

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
    parser.add_option('-o', '--out', dest='out',
                      action='store', default=False,
                      help = "optional file path for saving the image")

    return parser

def main():
    (options, args) = get_parser().parse_args()
 
    input = open(options.filename, 'r') if options.filename else sys.stdin


    df = pd.read_csv(input, sep = options.delim,
                     header = 0 if options.header else None)

    if options.x in df.columns:
        x = df[options.x]
    elif options.x.isdigit() and int(options.x) < df.shape[1]:
        x = df.iloc[:,int(options.x)]
    else:
        raise LookupError("Unknown X column: %s" % options.x)

    if options.y in df.columns:
        y = df[options.y]
    elif options.x.isdigit()  and int(options.y) < df.shape[1]:
        y = df.iloc[:, int(options.y)]
    else:
        raise LookupError("Unknown X column: %s" % options.x)


    hexbin(x.values, y.values,
           gridsize=int(options.bins),
           bins="log" if options.log_scale else None) 
    xlabel(x.name)
    ylabel(y.name)
    colorbar()

    try:
        import seaborn as sns
        sns.set_style("darkgrid")
    except:
        pass

    if options.out:
        savefig(options.out)
    else:
        show()


if __name__ == '__main__':
    main()
