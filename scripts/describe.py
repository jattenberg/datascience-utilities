#!/usr/local/bin/python
from scipy.stats import mstats, normaltest
import sys
from optparse import OptionParser
import numpy as np


def present(key, value):
    return key + " : " + str(value)

def trimean(values):
    return (mstats.scoreatpercentile(values, 25) + 2.0*mstats.scoreatpercentile(values, 50) + mstats.scoreatpercentile(values, 75))/4.0

def midhinge(values):
    return (mstats.scoreatpercentile(values, 25) + mstats.scoreatpercentile(values, 75))/2.0

parser = OptionParser(usage="""presents a range of standard descriptive statistics
on a single column of numerical data
perl -e 'for($i = 0; $i < 10000; $i++){print rand(), "\n"}' | python describe.py | column -t
Usage %prog [options]                                                                                
""")

parser.add_option('-f', '--file',
                  action = 'store', dest = 'filename', default=False)

(options, args) = parser.parse_args()

input = open(options.filename, 'r') if options.filename else sys.stdin

observed_values = []

for line in input:
    observed_values.append(float(line.strip()))

np_values = np.array(observed_values)

output = [
    present("Length", len(np_values)),
    present("Unique", len(np.unique(np_values))),
    present("Min", np_values.min()),
    present("Max", np_values.max()),
    present("Range", np_values.max() - np_values.min()),
    present("Q1", mstats.scoreatpercentile(np_values, 25)),
    present("Q2", mstats.scoreatpercentile(np_values, 50)),
    present("Q3", mstats.scoreatpercentile(np_values, 75)),
    present("Trimean", trimean(np_values)),
    present("Minhinge", midhinge(np_values)),
    present("Mean", np_values.mean()),
    present("Variance", mstats.variation(np_values)),
    present("Mode", mstats.mode(np_values)[0][0]),
    present("Skewness", mstats.skew(np_values)),
    present("Kurtosis", mstats.kurtosis(np_values)),
    ]

print "\n".join(output)

