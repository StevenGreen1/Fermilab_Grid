#!/bin/bash

for momentum in 4
do
    samweb prestage-dataset --defname=mcc10_protodune_beam_p${momentum}GeV_cosmics_3ms_sce_mcc10.0
done
