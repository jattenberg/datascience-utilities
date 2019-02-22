"""
Copyright (c) Josh Attenberg

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
from math import sqrt

def main():

    treatment_successes = float(sys.argv[1])
    treatment_failures = float(sys.argv[2])

    baseline_successes = float(sys.argv[3])
    baseline_failures = float(sys.argv[4])
    n_treatment = treatment_successes + treatment_failures
    n_baseline = baseline_successes + baseline_failures

    p_treatment = treatment_successes/n_treatment
    p_baseline = baseline_successes/n_baseline

    p_hat = (treatment_successes + baseline_successes)/(n_treatment + n_baseline)

    print (abs((p_treatment - p_baseline)/sqrt(p_hat*(1-p_hat)*(1.0/n_baseline + 1.0/n_treatment))))

if __name__ == "__main__":
    main()
