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
