#!/usr/local/bin/python
# generates data drawn from a gaussian distribution
# useful for testing a variety of processes
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

from optparse import OptionParser
from numpy.random import normal, lognormal, seed


def get_parser():
    parser = OptionParser("""generates a number of draws from a gaussian distribution.
    Observations are separated by new lines. if mean and stddev are lists, dim must match
    the number of entries in these lists
    Usage: %prog [options]""")

    parser.add_option("-n", "--number", action = 'store', dest = 'num', default = 100,
                      help = "number of draws to make")
    parser.add_option("-m", "--mean", action = 'store', dest = 'mean', default = "0",
                      help = "float or comma separated list of floats, 'center of the distribution'")
    parser.add_option("-s", "--stddev", action = 'store', dest = 'std', default = "1",
                      help = "float or comma separated list of floats, standard deviation of the generating distribution")
    parser.add_option("-S", "--seed", action = 'store', dest = 'seed',
                      help = "seed for random number generation")
    parser.add_option("-D", "--dim", action = 'store', dest = 'dim', default = "1",
                      help = "dimension- number of draws per line")
    parser.add_option("-d", "--delim", action = 'store', dest = 'delim', default = "\t",
                      help = "delimiter to separate columns in multidimensional output")
    parser.add_option("-L", "--lognormal", action = 'store_true', dest = 'lognormal',
                      help = "sample from the log-normal distribution instead of the normal distribution")
    return parser

def main():
    
    (options, args) = get_parser().parse_args()

    assert int(options.dim) > 0

    seed(int(options.seed) if options.seed else None)

    dist = lognormal if options.lognormal else normal
    mean = [float(m) for m in options.mean.split(",")] if "," in options.mean else float(options.mean)
    std = [float(s) for s in options.std.split(",")] if "," in options.std else float(options.std)
    dim = int(options.dim)
    
    for i in range(int(options.num)):
        print (options.delim.join(["%s" % x for x in dist(mean, std, dim)]))

if __name__ == "__main__":
    main()
