#!/bin/bash

# assumes python 3.6, pip, virtualenv

virtualenv venv
source venv/bin/activate
pip install -e . 

printf "\n\n\n\n"
echo "========================================================================"
echo "consider adding these to your profile!"
echo "========================================================================"
printf "\n\n"

echo "alias plot_hex=`pwd`/venv/bin/plot_hex"
echo "alias plot_xy=`pwd`/venv/bin/plot_xy"
echo "alias plot_hist=`pwd`/venv/bin/plot_hist"
echo "alias describe=`pwd`/venv/bin/describe"
echo "alias ztest=`pwd`/venv/bin/ztest"
echo "alias normal=`pwd`/venv/bin/normal"
echo "alias exponential=`pwd`/venv/bin/exponential"
echo "alias poisson=`pwd`/venv/bin/poisson"
echo "alias reservoir_sample=`pwd`/venv/bin/reservoir_sample"
echo "alias histogram=\"bash `pwd`/scripts/histogram.sh\""
echo "alias shuffle_lines=\"perl `pwd`/scripts/shuffleLines.pl\""

printf "\n\n"
