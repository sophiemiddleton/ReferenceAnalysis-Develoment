/*
Driving function for analysis
*/

#include <fstream>
#include<iostream>
//#include "ReferenceAna/inc/Mu2eAna.hh"
#include "ReferenceAna/inc/Likelihood.hh"

#include "TrkAna/inc/CrvHitInfoReco.hh"
#include "TrkAna/inc/MVAResultInfo.hh"
#include "TrkAna/inc/TrkInfo.hh"

using namespace std;
using namespace rootfitter;

TString Fpath = "/exp/mu2e/app/users/sophie/ProductionEnsembles_v2/py-ana/trkana/";


TTree *ImportNTuple(TString filename){
  TFile *f = TFile::Open(Fpath+filename);
  TTree *trkana = (TTree*)f->Get("TrkAna/trkana");  
  return trkana;
}

TH1F *GetRecoHist(TTree* trkana, bool usecuts){
  TH1F* hist_mom1 = new TH1F("hist_mom1", "", 100, 95,106);
  TString recocuts = "";
  if(usecuts){
    recocuts = "demfit.sid==0 && demlh.t0 > 700 && demlh.t0err < 0.9 && demtrkqual.result > 0.2 && dem.nactive > 20 && demlh.maxr < 680";
  }
  trkana->Draw("demfit.mom.R()>>hist_mom1", recocuts, "HIST");
  return hist_mom1;
}

TH1F* make_CRV_cuts(TTree *trkana, bool usecuts){
    std::vector<std::vector<mu2e::TrkFitInfo> >* tracks = 0;
    trkana->SetBranchAddress("demfit", &tracks);

    std::vector<mu2e::CrvHitInfoReco>* crvcoincs = 0;
    trkana->SetBranchAddress("crvcoincs", &crvcoincs);
    
    mu2e::MVAResultInfo* trkquals = 0;
    trkana->SetBranchAddress("demtrkqual", &trkquals);
    
    std::vector<std::vector<mu2e::LoopHelixInfo>>* lhs;
    trkana->SetBranchAddress("demlh", &lhs);
    
    TH1F* hist_mom1 = new TH1F("hist_mom1","",100, 95, 110);
    
    unsigned int n_events = trkana->GetEntries();
    for (unsigned int i_event = 0; i_event < n_events; ++i_event) {
      trkana->GetEntry(i_event);
      bool passes_lhcuts = false;
      for (auto& lh : *lhs) { 
        if(lh.size() > 0){ 
          if(usecuts and trkquals->result > 0.2 and lh[0].t0> 700 and lh[0].t0err < 0.9 and lh[0].maxr<680){
            passes_lhcuts = true;
          } if(!usecuts) passes_lhcuts = true;
        }
      }
      for (auto& track : *tracks) {
        for (auto& fit : track) {
          if (fit.sid == 0) {
            double track_time = fit.time;
            bool crvhit = false;
            for (auto& crvcoinc : *crvcoincs) {
              double crvcoinc_time = crvcoinc.time;
              if (std::fabs(crvcoinc_time - track_time) < 150) {
                crvhit = true;
              }
            }
            if (!crvhit and passes_lhcuts) {
              hist_mom1->Fill(fit.mom.R());
              
            }
          }
        }
      }
    }
    return hist_mom1;
}



void RunFit(TH1F* histmom, TString Run, bool cuts){
  std::cout<<" calling root-fitter ...  "<<std::endl;
  Likelihood *lh = new Likelihood();
  RooFitResult *result = lh->CalculateBinnedLikelihood(histmom, Run, cuts);
  std::cout<<" Mu2e Ana Result "<< result << std::endl;
}

int main(int argc, char* argv[]){
  std::cout<<"========== Welcome to Mu2eAna =========="<<std::endl;
  std::cout<<"-------- Analyzing "<<argv[2]<<" ------------"<<std::endl;
  
  TString filename = argv[1]; // TrkAna NTuple
  TString runname = argv[2]; // e.g. pass0a
  bool usecuts = argv[3]; //true or false
  
  TTree *trkana = ImportNTuple(filename);
  if(runname == "pass0a") {
    TH1F *histmom = GetRecoHist(trkana, usecuts);
    RunFit(histmom, runname, usecuts);
  }
  if(runname == "pass0b") {
    TH1F *histmom = make_CRV_cuts(trkana, usecuts);
    RunFit(histmom, runname, usecuts);
  }
  return 0;
}
