#!/usr/local/bin/python
from scipy.stats import mstats, normaltest, sem
import sys
from optparse import OptionParser
import numpy as np
import pandas as pd


def get_data(column, np_values):
    output = [
        present("Column", column),
        present("Length", len(np_values)),
        present("Unique", len(np.unique(np_values))),
        present("Min", np_values.min()),
        present("Max", np_values.max()),
        present("Mid-Range", (np_values.max() - np_values.min())/2),
        present("Range", np_values.max() - np_values.min()),
        present("Q1", mstats.scoreatpercentile(np_values, 25)),
        present("Q2", mstats.scoreatpercentile(np_values, 50)),
        present("Q3", mstats.scoreatpercentile(np_values, 75)),
        present("Trimean", trimean(np_values)),
        present("Minhinge", midhinge(np_values)),
        present("Mean", np_values.mean()),
        present("Variance", mstats.variation(np_values)),
        present("StdDev", np.std(np_values)),
        present("Mode", mstats.mode(np_values)[0][0]),
        present("Skewness", mstats.skew(np_values)),
        present("Kurtosis", mstats.kurtosis(np_values)),
        present("StdErr", sem(np_values)), 
        present("Normal-P-value", normaltest(np_values)[1])
        ]
    return output

def present(key, value):
    return key + " : " + str(value)

def trimean(values):
    return (mstats.scoreatpercentile(values, 25) + 2.0*mstats.scoreatpercentile(values, 50) + mstats.scoreatpercentile(values, 75))/4.0

def midhinge(values):
    return (mstats.scoreatpercentile(values, 25) + mstats.scoreatpercentile(values, 75))/2.0

parser = OptionParser(usage="""presents a range of standard descriptive statistics
on a single column of numerical data
perl -e 'for($i = 0; $i < 20; $i++){print rand(), "\t", rand(), "\t", rand(), "\n"}' | python describe.py
Usage %prog [options]                                                                                
""")

parser.add_option('-f', '--file',
                  action = 'store', dest = 'filename', default=False)
parser.add_option('-H', '--header', 
                  action = 'store_true', dest = 'header', default = None)
parser.add_option('-d', '--delim',
                  action='store', dest='delim', default="\t") 

(options, args) = parser.parse_args()

input = open(options.filename, 'r') if options.filename else sys.stdin

df = pd.read_csv(input, sep = options.delim,
                 header = 0 if options.header else None)

description = []
for column in df.columns:
    output = get_data(column, df[column].values)
    description.append("\n".join(output))

print "\n\n".join(description)

