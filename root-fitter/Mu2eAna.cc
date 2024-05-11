/*
Driving function for analysis
*/

#include <fstream>
#include<iostream>
#include "Mu2eAna.hh"
#include "Likelihood.hh"
using namespace std;

TString Fpath = "/exp/mu2e/app/users/sophie/ProductionEnsembles_v2/py-ana/trkana/";


TTree *ImportNTuple(TString filename){
  TFile *f = TFile::Open(Fpath+filename);
  TTree *trkana = (TTree*)f->Get("TrkAna/trkana");  
  return trkana;
}

TH1F *GetRecoHist(TTree* trkana, bool usecuts){
  TH1F* hist_mom1 = new TH1F("hist_mom1", "", 100, 95,105);
  TString recocuts = "";
  if(usecuts){
    recocuts = "demfit.sid==0 && demlh.t0 > 700 && demlh.t0err < 0.9 && demtrkqual.result > 0.2 && dem.nactive > 20 && demlh.maxr < 680";
  }
  trkana->Draw("demfit.mom.R()>>hist_mom1", recocuts, "HIST");
  return hist_mom1;
}

void RunFit(TH1F* histmom, TString Run, bool cuts){
  std::cout<<" calling root-fitter ...  "<<std::endl;
  Likelihood *lh = new Likelihood();
  RooFitResult *result = lh->CalculateLikelihood(histmom, Run, cuts);
  std::cout<<" Mu2e Ana Result "<< result << std::endl;
}

int main(int argc, char* argv[]){
  std::cout<<"========== Welcome to Mu2eAna =========="<<std::endl;
  std::cout<<"-------- Analyzing "<<argv[2]<<" ------------"<<std::endl;
  
  TString filename = argv[1]; // TrkAna NTuple
  TString runname = argv[2]; // e.g. pass0a
  bool usecuts = argv[3]; //true or false
  
  TTree *trkana = ImportNTuple(filename);
  TH1F *histmom = GetRecoHist(trkana, usecuts);
  RunFit(histmom, runname, usecuts);
  return 0;
}
