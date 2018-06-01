#!/bin/bash

#for momenta in -6 -4 -3 -2 2 3 4 6 # DONE -7 -5 -1 1 5 7 
for momenta in 6 #-3 -2 2 4
do
#    project.py --xml ConfigFile_ProtoDUNE_beam_${momenta}GeV_cosmics_3ms_mcc10.xml --stage pndr --submit
    project.py --xml ConfigFile_ProtoDUNE_beam_${momenta}GeV_cosmics_3ms_sce_mcc10.xml --stage pndr --submit
done

