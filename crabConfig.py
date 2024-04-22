from CRABClient.UserUtilities import config
config = config()

config.General.requestName = '2017ppBmesons_hl_TEST'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runForestAOD_pp_DATA_94X_onlyBfinder.py'

config.Data.inputDataset = '/DoubleMuon/Run2017G-17Nov2017-v1/AOD'
config.Data.inputDBS = "global"
#config.Data.splitting = "LumiBased"                                                 
config.Data.unitsPerJob = 20
#config.Data.lumiMask = 'Cert_306546-306826_5TeV_EOY2017ReReco_Collisions17_JSON_MuonPhys.txt'
config.Data.publication = False
config.Data.outputDatasetTag = '2017ppbmesons_hl'

config.Data.outLFNDirBase = '/store/user/legoinha/'
config.Site.storageSite = 'T2_PT_NCG_Lisbon'


config.General.transferLogs = False
config.JobType.numCores = 1
config.JobType.maxMemoryMB = 2000
config.JobType.allowUndistributedCMSSW = True

#NJOBS = 500  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = -1
 




