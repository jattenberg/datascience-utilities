#!/usr/local/bin/python
# generates data drawn from a gaussian distribution
# useful for testing a variety of processes

from optparse import OptionParser
from numpy.random import normal


parser = OptionParser("""generates a number of draws from a gaussian distribution.
Observations are separated by new lines.
Usage: %prog [options]""")

parser.add_option("-n", "--number", action = 'store', dest = 'num', default = 100,
                  help = "number of draws to make")
parser.add_option("-m", "--mean", action = 'store', dest = 'mean', default = 0,
                  help = "mean of the generating distribution")
parser.add_option("-s", "--stddev", action = 'store', dest = 'std', default = 1,
                  help = "standard deviation of the generating distribution")

(options, args) = parser.parse_args()

for i in range(int(options.num)):
    print normal(float(options.mean), float(options.std))
