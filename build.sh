#!/bin/bash

# assumes python 3.6, pip, virtualenv

virtualenv venv
source venv/bin/activate
pip install -e . 



echo "consider adding this to your profile!"
echo "alias plot_hex=`pwd`/venv/bin/plot_hex"
echo "alias plot_xy=`pwd`/venv/bin/plot_xy"
echo "alias plot_hist=`pwd`/venv/bin/plot_hist"
echo "alias describe=`pwd`/venv/bin/describe"
echo "alias ztest=`pwd`/venv/bin/ztest"
echo "alias normal=`pwd`/venv/bin/normal"
echo "alias reservoir_sample=`pwd`/venv/bin/reservoir_sample"
echo "alias histogram=`pwd`/scripts/histogram.sh"
