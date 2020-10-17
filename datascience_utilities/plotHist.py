#plotHist by @jattenberg, Dec 2012
#reads columns of floating point values in a file or a unix pipe
#builds a histogram for each column and plots it
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
import matplotlib.pyplot as plt
from math import log
import pandas as pd
from optparse import OptionParser
import seaborn as sns

#expects a list of pairs, x, #x

def get_parser():
    parser = OptionParser(usage ="""                                                                 
    Generate a histogram from new-line separated numerical data of the form x1, x2, ...
    each column containing values form a particular series to form a histogram over
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
    parser.add_option('-o', '--out', dest='out',
                      action='store', default=False,
                      help = "optional file path for saving the image")
    parser.add_option('-i', '--ignore', dest='ignore',
                      action='store',
                      help = "ignore the specified colums. can be a column name or column index (from 0). specifiy multiple values separated by commas")

    return parser

def main():
    
    (options, args) = get_parser().parse_args()
 
    input = open(options.filename, 'r') if options.filename else sys.stdin


    df = pd.read_csv(input, sep = options.delim,
                     header = 0 if options.header else None)

    if options.ignore:
        tdf = df.copy()
        to_ignores = options.ignore.split(",")
        for to_ignore in to_ignores:
            if to_ignore in df.columns:
                c = df[to_ignore]
            elif to_ignore.isdigit() and int(to_ignore) < df.shape[1]:
                c = df.iloc[:, int(to_ignore)]
            else:
                raise LookupError("Unknown column to ignore: %s" % to_ignore)

            tdf = tdf.drop(c.name, axis=1)
        
        df = tdf
        print ("remaining columns: %s" % ", ".join(["'%s'" % x for x in df.columns.values]))

    (df.applymap(lambda x : log(x)) if options.log_scale else df).hist(bins=int(options.bins))

    try:
        import seaborn as sns
        sns.set_style("darkgrid")
    except:
        pass

    if options.out:
        plt.savefig(options.out)
    else:
        plt.show()


if __name__ == "__main__":
    main()


