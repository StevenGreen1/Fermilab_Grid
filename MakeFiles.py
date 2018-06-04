import sys
import os
import re
import subprocess

tag = 3

templateFile = 'ConfigFile_Template.xml'
base = open(templateFile,'r')
content = base.read()
base.close()

eventsToProcess = [
                      { 'EventType': "beam_cosmics", 'EventsPerFile' : 40, 'Momenta':  [4], 'SpaceChargeEffect': True, 'AnalysisTag': tag }
                  ]

jobName = 'UpdatedReconstruction'
larsoftVersion = 'v06_77_00'

# These files have to live on persistent
initScript   = '/pnfs/dune/persistent/users/sgreen/LocalTarball/larsoft_v06_77_00_sample_production/init.sh'
fclScript    = '/pnfs/dune/persistent/users/sgreen/LocalTarball/larsoft_v06_77_00_sample_production/my_protoDUNE_reco_3ms.fcl'
localTarball = '/pnfs/dune/persistent/users/sgreen/LocalTarball/larsoft_v06_77_00_sample_production/local.tar'

# Info on jobs expected lifetime https://cdcvs.fnal.gov/redmine/projects/larbatch/wiki/User_guide

for eventSelection in eventsToProcess:
    momenta = eventSelection['Momenta']
    eventsPerFile = eventSelection['EventsPerFile']
    spaceChargeEffect = eventSelection['SpaceChargeEffect']
    analysisTag = eventSelection['AnalysisTag']

    spaceChargeEffectString = ''
    if spaceChargeEffect:
        spaceChargeEffectString = '_sce'

    for momentum in momenta:
        # This .list file is used for counting the number of files and events per job.  The samweb inputdef is used to find the files stored on tape.
        defname = 'mcc10_protodune_beam_p' + str(momentum) + 'GeV_cosmics_3ms' + spaceChargeEffectString + '_mcc10.0'

        proc = subprocess.Popen(['samweb', 'count-definition-files', 'mcc10_protodune_beam_p' + str(momentum) + 'GeV_cosmics_3ms' + spaceChargeEffectString + '_mcc10.0'], stdout=subprocess.PIPE)
        numberOfFiles = int(proc.stdout.read())
        print "Number of files in " + defname + " is " + str(numberOfFiles)

        # Guide: https://cdcvs.fnal.gov/redmine/projects/uboonecode/wiki/Tutorial_for_Analyzers_and_Using_the_Gird
        # numberOfJobs is the number of jobs that are used provessing the entire data set.  In this case each job should process 40, this takes three times the age of the known universe so tell larsoft that the memory and time needed will be big.
        numberOfJobs = numberOfFiles 

        # numberOfEvents is the maximum number of events that should be processed
        numberOfEvents = eventsPerFile * numberOfFiles

        newContent = re.sub('Momentum', str(momentum), content)
        newContent = re.sub('NumberOfJobs', str(numberOfJobs), newContent)
        newContent = re.sub('NumberOfEvents', str(numberOfEvents), newContent)
        newContent = re.sub('Tag', str(tag), newContent)
        newContent = re.sub('InputDef', defname, newContent)
        newContent = re.sub('InitScript', initScript, newContent)
        newContent = re.sub('FclScript', fclScript, newContent)
        newContent = re.sub('LocalTarballName', localTarball, newContent)
        newContent = re.sub('LArSoftVersion', larsoftVersion, newContent)
        newContent = re.sub('JobName', jobName, newContent)

        if not spaceChargeEffect:
            newContent = re.sub('SpaceCharge_','', newContent)

        newGridScriptName = 'ConfigFile_ProtoDUNE_beam_' + str(momentum) + 'GeV_cosmics_3ms' + spaceChargeEffectString + '_mcc10.xml'
        with open(newGridScriptName ,"w") as script:
            script.write(newContent)

