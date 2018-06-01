#!/bin/bash

for momenta in 6 
do
    TARGET_DIR="/pnfs/dune/scratch/users/sgreen/v06_63_00_Pndr_${momenta}GeV_Beam_Cosmics_SpaceCharge_v2/pndr/"
    FILENAME="PndrFiles_ProtoDUNE_beam_${momenta}GeV_cosmics_3ms_sce_mcc10.txt"
    echo "Finding pndr files in ${TARGET_DIR}"
    find ${TARGET_DIR} -name *.pndr >> ${FILENAME}
    echo "List saved to ${FILENAME}. "
done
