#!/usr/local/bin/python
from scipy.stats import stats, normaltest, sem, bayes_mvs
import sys
from optparse import OptionParser
import numpy as np
import pandas as pd
from math import log

def get_nonnumeric(column, np_values):

    data = np_values.describe();
    output = [ present("Column", column) ]
    for id in data.index:
        output.append(present(id.capitalize(), data[id]))
    return output

def get_data(column, np_values, alpha):

    mvs = bayes_mvs(np_values, alpha)

    #report these metrics
    output = [
        present("Column", column),
        present("Length", len(np_values)),
        present("Unique", len(np.unique(np_values))),
        present("Min", np_values.min()),
        present("Max", np_values.max()),
        present("Mid-Range", (np_values.max() - np_values.min())/2),
        present("Range", np_values.max() - np_values.min()),
        present("Mean", np_values.mean()),
        present("Mean-%s-CI" % alpha, tupleToString(mvs[0][1])),
        present("Variance", mvs[1][0]),
        present("Var-%s-CI" % alpha, tupleToString(mvs[1][1])),
        present("StdDev", mvs[2][0]),
        present("Std-%s-CI" % alpha, tupleToString(mvs[2][1])),
        present("Mode", stats.mode(np_values)[0][0]),
        present("Q1", stats.scoreatpercentile(np_values, 25)),
        present("Q2", stats.scoreatpercentile(np_values, 50)),
        present("Q3", stats.scoreatpercentile(np_values, 75)),
        present("Trimean", trimean(np_values)),
        present("Minhinge", midhinge(np_values)),
        present("Skewness", stats.skew(np_values)),
        present("Kurtosis", stats.kurtosis(np_values)),
        present("StdErr", sem(np_values)),
        present("Normal-P-value", normaltest(np_values)[1])
        ]
    return output

#this prints a bit nicer than tuples standard toString
def tupleToString(tuple):
    return "(%s, %s)" % tuple

def present(key, value):
    return key + " : " + str(value)

def trimean(values):
    return (stats.scoreatpercentile(values, 25) + 2.0*stats.scoreatpercentile(values, 50) + stats.scoreatpercentile(values, 75))/4.0

def midhinge(values):
    return (stats.scoreatpercentile(values, 25) + stats.scoreatpercentile(values, 75))/2.0

parser = OptionParser(usage="""presents a range of standard descriptive statistics
on columns of numerical data
perl -e 'for($i = 0; $i < 20; $i++){print rand(), "\\t", rand(), "\\t", rand(), "\\n"}' | python describe.py
Usage %prog [options]                                                                                
""")

parser.add_option('-f', '--file',
                  action = 'store', dest = 'filename', default=False,
                  help="[optional] use a specified file instead of reading from stdin")
parser.add_option('-H', '--header', 
                  action = 'store_true', dest = 'header', default = None,
                  help="treat the first row as column headers")
parser.add_option('-d', '--delim',
                  action='store', dest='delim', default="\t",
                  help="delimiter seperating columns in input") 
parser.add_option('-a', '--alpha',
                  action='store', dest='alpha', default=0.9,
                  help="confidence value used in interval estimation") 
parser.add_option('-s', '--simple', 
                  action = 'store_true', dest = 'simple', default = False,
                  help="abbreviated, simplified output")

(options, args) = parser.parse_args()

input = open(options.filename, 'r') if options.filename else sys.stdin

df = pd.read_csv(input, sep = options.delim,
                 header = 0 if options.header else None)

description = []
num_columns = []
for column in df.columns:
    #only consider numeric columns
    if df[column].dtype.kind == 'i' or df[column].dtype.kind == 'f':
        output = get_data(column, df[column], float(options.alpha))
        num_columns.append(column)
        description.append("\n".join(output))
    else:
        output = get_nonnumeric(column, df[column])
        description.append("\n".join(output))

print "\n\n".join(description)

if not options.simple:
    print "\n\nCovariances:"
    print df[num_columns].cov()

    print "\n\nCorrelations:"
    print df[num_columns].corr()
