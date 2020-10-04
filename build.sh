#!/bin/bash

# assumes python 3.6, pip, virtualenv
iterm=$1

hash pipx
if [ "$?" != "0" ]; then
  pip install pipx;
fi

pipx uninstall . 

if [ "$iterm" = "iterm" ]; then
    echo "building with iterm inline plotting"
    pipx install .[iterm]
else
    pipx install .
fi

pipx ensurepath

printf "\n\n\n\n"
echo "========================================================================"
echo "consider adding these to your profile!"
echo "========================================================================"
printf "\n\n"

if [ "$iterm" = "iterm" ]; then
    echo 'export MPLBACKEND="module://itermplot"'
fi

echo "alias histogram=\"bash `pwd`/scripts/histogram.sh\""
echo "alias shuffle_lines=\"perl `pwd`/scripts/shuffleLines.pl\""

printf "\n\n"
