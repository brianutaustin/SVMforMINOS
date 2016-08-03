#! /use/bin/python

from ROOT import TFile
from ROOT import gDirectory
import numpy as np
from sklearn import svm

# open the file
myfile = TFile('./I6.0E13fullDST.root')

# retrieve the ntuple of interest
trainchain = gDirectory.Get('trainPID')
trainentries = trainchain.GetEntriesFast()
traindata = np.zeros((200000,4))
trainoutput = np.zeros((200000,))
#for jentry in xrange(trainentries):
for jentry in range(0,200000):
    # get the next tree in the chain and verify

    ientry = trainchain.LoadTree(jentry)
    if ientry < 0:
        break
    # copy next entry into memory and verify
    nb = trainchain.GetEntry(jentry)
    if nb <= 0:
        continue

    traindata[jentry, 0] = trainchain.knn01TrkActivePlanes
    traindata[jentry, 1] = trainchain.knn10TrkMeanPh
    traindata[jentry, 2] = trainchain.knn20LowHighPh
    traindata[jentry, 3] = trainchain.knn40TrkPhFrac
    trainoutput[jentry] = trainchain.signalMC
# Normalize the train data
for i in range(0, 4):
    tdmean = np.mean(traindata[:,i])
    tdsigma = np.std(traindata[:,i])
    traindata[:,i] = (traindata[:,i] - tdmean)/tdsigma



# retrieve the ntuple of interest
testchain = gDirectory.Get('test')
testentries = testchain.GetEntriesFast()
testdata = np.zeros((testentries,4))
testoutput = np.zeros((testentries,))
#testdata = np.zeros((10000,4))
#testoutput = np.zeros((10000,))
#for jentry in xrange(testentries):
for jentry in range(0,testentries):
    # get the next tree in the chain and verify
    ientry = testchain.LoadTree(jentry)
    if ientry < 0:
        break
    # copy next entry into memory and verify
    nb = testchain.GetEntry(jentry)
    if nb <= 0:
        continue
    testdata[jentry, 0] = testchain.knn01TrkActivePlanes
    testdata[jentry, 1] = testchain.knn10TrkMeanPh
    testdata[jentry, 2] = testchain.knn20LowHighPh
    testdata[jentry, 3] = testchain.knn40TrkPhFrac
    #testdata[jentry, 4] = testchain.roID
    testoutput[jentry] = testchain.signalMC
# Normalize the train data
for i in range(0, 4):
    tdmean = np.mean(traindata[:,i])
    tdsigma = np.std(traindata[:,i])
    traindata[:,i] = (traindata[:,i] - tdmean)/tdsigma



# Training data
clf = svm.SVC()
clf.fit(traindata, trainoutput)
validationoutput = clf.predict(testdata)
