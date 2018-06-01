import sys
import os
import re
import subprocess

tag = 1

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
fclScript    = '/pnfs/dune/persistent/users/sgreen/LocalTarball/larsoft_v06_77_00_sample_production/protoDUNE_reco_3ms.fcl'
localTarball = '/pnfs/dune/persistent/users/sgreen/LocalTarball/larsoft_v06_77_00_sample_production/local.tar'

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

        newContent = re.sub('Momentum', str(momentum), content)
        newContent = re.sub('NumberOfFiles', str(numberOfFiles), newContent)
        newContent = re.sub('NumberOfJobs', str(eventsPerFile * numberOfFiles), newContent)
        newContent = re.sub('Tag', str(tag), newContent)
        newContent = re.sub('InputDef', defname, newContent)
        newContent = re.sub('InitScript', initScript, newContent)
        newContent = re.sub('FclScript', fclScript, newContent)
        newContent = re.sub('LocalTarball', localTarball, newContent)
        newContent = re.sub('LArSoftVersion', larsoftVersion, newContent)
        newContent = re.sub('JobName', jobName, newContent)

        if not spaceChargeEffect:
            newContent = re.sub('SpaceCharge_','', newContent)

        newGridScriptName = 'ConfigFile_ProtoDUNE_beam_' + str(momentum) + 'GeV_cosmics_3ms' + spaceChargeEffectString + '_mcc10.xml'
        with open(newGridScriptName ,"w") as script:
            script.write(newContent)

