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

xs = []

for line in input:
    ct = ct+1.
    x = float(line.rstrip())
    delta = x - mean
    mean = mean + delta/ct
    var_part = var_part + delta*(x - mean)
    xs.append(x)


variance = var_part/(ct-1)
skewness = 0.
kurtosis = 0.

for x in xs:
    skewness = skewness + (x-mean)**3
    kurtosis = kurtosis + (x-mean)**4

kurtosis = kurtosis/float(len(xs))
skewness = skewness/float(len(xs))

skewness = skewness / (variance**1.5)
kurtosis = kurtosis / (variance / 2)

print "skewness: %f, kurtosis: %f" % (skewness,  kurtosis)
