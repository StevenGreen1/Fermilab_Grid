#!/bin/bash

for momenta in 4 
do
    TARGET_DIR="/pnfs/dune/scratch/users/sgreen/v06_77_00_UpdatedReconstruction_${momenta}GeV_Beam_Cosmics_SpaceCharge_v2/updatedreco/"
    FILENAME="RootFiles_ProtoDUNE_beam_${momenta}GeV_cosmics_3ms_sce_mcc10.txt"
    echo "Finding root files in ${TARGET_DIR}"
    find ${TARGET_DIR} -name mcc10_protodune_beam_p4GeV_cosmics_3ms_sce_*_merged0_reco.root >> ${FILENAME}
    echo "List saved to ${FILENAME}. "
done
