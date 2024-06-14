from CRABClient.UserUtilities import config
config = config()

config.General.requestName = '2017ppDATA_bQ'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runForestAOD_pp_DATA_94X_onlyBfinder.py'

config.Data.inputDataset = '/DoubleMuon/Run2017G-17Nov2017-v1/AOD'
config.Data.inputDBS = "global"

config.Data.splitting = "LumiBased"                                                 
config.Data.unitsPerJob = 20
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/5TeV/ReReco/Cert_306546-306826_5TeV_EOY2017ReReco_Collisions17_JSON_MuonPhys.txt'

config.Data.publication = False
config.Data.outputDatasetTag = '2017ppDATA_bQ_hadronization'

#config.Data.outLFNDirBase = '/store/user/legoinha/'
config.Site.storageSite = 'T2_PT_NCG_Lisbon'


config.JobType.numCores = 1
config.JobType.maxMemoryMB = 2000
config.JobType.allowUndistributedCMSSW = True

config.Data.totalUnits = -1
 




