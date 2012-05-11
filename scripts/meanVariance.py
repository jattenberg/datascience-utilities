#!/usr/bin/python
import sys


 
if len(sys.argv) == 2:
    input = open(sys.argv[1],'r')
elif len(sys.argv) == 1:
    input = sys.stdin;
else:
    sys.exit("Usage:  python mean.py <?file>")
 
ct = 0.
mean = 0.
var_part = 0.

for line in input:
    ct = ct+1.
    x = float(line.rstrip())
    delta = x - mean
    mean = mean + delta/ct
    var_part = var_part + delta*(x - mean)
    

print "mean: %f, variance: %f" % (mean,  var_part/(ct-1))

