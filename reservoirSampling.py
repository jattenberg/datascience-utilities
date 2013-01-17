#!/usr/bin/python
import sys
import random
from optparse import OptionParser


parser = OptionParser(usage="""performs reservoir sampling on input data to reduce the amount of
 input to reduce the amound of data to be processed
Usage %prog [options]""")

parser.add_option('-f', '--file',
                  action = 'store', dest = 'filename', default=False,
                  help="[optional] use a specified file instead of reading from stdin")
parser.add_option('-n', '--number',
                  action='store', dest='n', default=False,
                  help="the number of input lines to keep") 

(options, args) = parser.parse_args()

N = int(options.n) if options.n else int(args[0]) if len(args) >= 1 else 100
input = open(options.filename, 'r') if options.filename else sys.stdin 

sample = [];

for i, line in enumerate(input):
    if i < N:
        sample.append(line)
    elif i >= N and random.random() < N/float(i + 1):
        replace = random.randint(0, len(sample) - 1)
        sample[replace] = line
 
for line in sample:
    sys.stdout.write(line)
