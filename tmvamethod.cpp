#include <iostream>
#include <cstring>
#include <cmath>

#include "TFile.h"
#include "TTree.h"

#include "TMVA/Types.h"
#include "TMVA/Factory.h"
#include "TMVA/Tools.h"

int main() {
  TFile *f = new TFile("./I6.0E13fullDST.root");
  TFile *fout = new TFile("./TMVATestOut.root", "RECREATE");
  // Get the signal and background training and test trees from TFile source(s);
  TTree *sigTreeTrain = (TTree*)f->Get("trainS");
  TTree *bkgTreeTrain = (TTree*)f->Get("trainB");
  TTree *sigTreeTest  = (TTree*)f->Get("testS");
  TTree *bkgTreeTest  = (TTree*)f->Get("testB" );
  // Set the event weights (these weights are applied in
  // addition to individual event weights that can be specified)
  Double_t sigWeight  = 1.0;
  Double_t bkgWeight = 1.0;

  TMVA::Factory* factory = new TMVA::Factory("TMVATest", fout, "Classification");
  // Register the trees
  factory->AddSignalTree(sigTreeTrain, sigWeight, TMVA::Types::kTraining);
  factory->AddBackgroundTree(bkgTreeTrain, bkgWeight, TMVA::Types::kTraining);
  factory->AddSignalTree(sigTreeTest,  sigWeight, TMVA::Types::kTesting);
  factory->AddBackgroundTree(bkgTreeTest,  bkgWeight, TMVA::Types::kTesting);

  factory->AddVariable("knn01TrkActivePlanes",'I');
  factory->AddVariable("knn10TrkMeanPh",'F');
  factory->AddVariable("knn20LowHighPh",'F');
  factory->AddVariable("knn40TrkPhFrac",'F');

  return 0;
}
