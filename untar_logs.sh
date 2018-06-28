#!/bin/bash

for dir in */
do 
    cd $dir
    [[ -f Pandora_Events.pndr ]] && echo "Found" || tar -xvf log.tar ./Pandora_Events.pndr
    cd ../
done
