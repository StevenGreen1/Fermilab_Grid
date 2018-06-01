#!/bin/bash

for momenta in 4
do
    project.py --xml ConfigFile_ProtoDUNE_beam_${momenta}GeV_cosmics_3ms_sce_mcc10.xml --stage updatedreco --submit
done

