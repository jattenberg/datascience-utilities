import sys
from math import sqrt

treatment_successes = float(sys.argv[1])
treatment_failures = float(sys.argv[2])

baseline_successes = float(sys.argv[3])
baseline_failures = float(sys.argv[4])
n_treatment = treatment_successes + treatment_failures
n_baseline = baseline_successes + baseline_failures

p_treatment = treatment_successes/n_treatment
p_baseline = baseline_successes/n_baseline

p_hat = (treatment_successes + baseline_successes)/(n_treatment + n_baseline)

print abs((p_treatment - p_baseline)/sqrt(p_hat*(1-p_hat)*(1.0/n_baseline + 1.0/n_treatment)))
