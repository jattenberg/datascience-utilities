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
import random
from optparse import OptionParser


def get_parser():
    parser = OptionParser(usage="""performs reservoir sampling on input data to reduce the amount of
    input to reduce the amound of data to be processed
    Usage %prog [options]""")

    parser.add_option('-f', '--file',
                      action = 'store', dest = 'filename', default=False,
                      help="[optional] use a specified file instead of reading from stdin")
    parser.add_option('-n', '--number',
                      action='store', dest='n', default=False,
                      help="the number of input lines to keep")
    parser.add_option('-o', '--out',
                      action = 'store', dest = 'out', default=False,
                      help="[optional] write to a specified file instead of stdout")
    return parser

def main():
    (options, args) = get_parser().parse_args()

    N = int(options.n) if options.n else int(args[0]) if len(args) >= 1 else 100
    input = open(options.filename, 'r') if options.filename else sys.stdin 

    out = open(options.out, 'r') if options.out else sys.stdout
    sample = [];

    for i, line in enumerate(input):
        if i < N:
            sample.append(line)
        elif i >= N and random.random() < N/float(i + 1):
            replace = random.randint(0, len(sample) - 1)
            sample[replace] = line
 
    for line in sample:
        out.write(line)
    out.flush()
    out.close()

if __name__ == "__main__":
    main()
