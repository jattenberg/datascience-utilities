#!/bin/bash

set -e
# assumes python 3.6, pip, virtualenv
iterm=$1

if ! command -v pipx &> /dev/null 
then
    echo "pipx could not be found"
    pip install pipx;
else
  pipx_path=$(which pipx);
  echo "using pipx located at $pipx_path"
fi


pipx ensurepath
pipx uninstall . 

if [ "$iterm" = "iterm" ];
then
    echo "building with iterm inline plotting"
    pipx install .[iterm]
else
    pipx install .
fi


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
