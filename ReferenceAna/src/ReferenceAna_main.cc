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
#include "TrkAna/inc/SimInfo.hh"

using namespace std;
using namespace rootfitter;

TString Fpath = "/exp/mu2e/app/users/sophie/ProductionEnsembles_v2/py-ana/trkana/";


TTree *ImportNTuple(TString filename){
  TFile *f = TFile::Open(Fpath+filename);
  TTree *trkana = (TTree*)f->Get("TrkAna/trkana");  
  return trkana;
}

TH1F *GetRecoHist(TTree* trkana, bool usecuts, double mom_lo, double mom_hi){
  TH1F* hist_mom1 = new TH1F("hist_mom1", "", 100, mom_lo,mom_hi);
  TString recocuts = "";
  if(usecuts){
    recocuts = "demfit.sid==0 && demlh.t0 > 700 && demlh.t0err < 0.9 && demtrkqual.result > 0.2 && dem.nactive > 20 && demlh.maxr < 680";
  }
  trkana->Draw("demfit.mom.R()>>hist_mom1", recocuts, "HIST");
  return hist_mom1;
}

TTree* make_CRV_cuts_tree(TTree *trkana, bool usecuts, double mom_low, double mom_hi, std::tuple <double, double, double, double>& mcresults){
    std::vector<std::vector<mu2e::TrkFitInfo> >* tracks = 0;
    trkana->SetBranchAddress("demfit", &tracks);

    std::vector<mu2e::CrvHitInfoReco>* crvcoincs = 0;
    trkana->SetBranchAddress("crvcoincs", &crvcoincs);
    
    mu2e::MVAResultInfo* trkquals = 0;
    trkana->SetBranchAddress("demtrkqual", &trkquals);
    
    std::vector<std::vector<mu2e::LoopHelixInfo>>* lhs = 0;
    trkana->SetBranchAddress("demlh", &lhs);
    
    std::vector<std::vector<mu2e::SimInfo>>* sims = 0;
    trkana->SetBranchAddress("demmcsim", &sims);
    
    
    Float_t recomom;
    TTree *tree_recomom = new TTree("recomom","recomom");
    tree_recomom->Branch("recomom", &recomom, "recomom/F"); // reco mom
    double nCE = 0;
    double nDIO = 0;
    double nCosmics = 0;
    double nRPC = 0;
    unsigned int n_events = trkana->GetEntries();
    for (unsigned int i_event = 0; i_event < n_events; ++i_event) {
      bool passCE = false;
      bool passDIO = false;
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
              for (auto& sim : *sims) {
                for (auto& s : sim){
                  double startCode = s.startCode;
                  if(fit.mom.R() > mom_low and startCode == 166 and !passDIO ) { nDIO+=1; passDIO=true;}
                  if(fit.mom.R() > mom_low and fit.mom.R() < mom_hi and startCode == 167 and !passCE) { nCE +=1;passCE=true;}
                }
              }
              recomom = (fit.mom.R());
              tree_recomom->Fill();
            }
          }
        }
      }
    }
    mcresults = make_tuple(nCE,nDIO,nCosmics,nRPC);
    std::cout<<"MC Truth Count = nCE "<<nCE<<" nDIO "<<nDIO<<std::endl;
    return tree_recomom;
}
    
void PlotMC(){} // TODO - plot the momentum of the true CE's - where are they?

TH1F* make_CRV_cuts(TTree *trkana, bool usecuts, double mom_low, double mom_hi, std::tuple <double, double, double, double>& mcresults){
    std::vector<std::vector<mu2e::TrkFitInfo> >* tracks = 0;
    trkana->SetBranchAddress("demfit", &tracks);

    std::vector<mu2e::CrvHitInfoReco>* crvcoincs = 0;
    trkana->SetBranchAddress("crvcoincs", &crvcoincs);
    
    mu2e::MVAResultInfo* trkquals = 0;
    trkana->SetBranchAddress("demtrkqual", &trkquals);
    
    std::vector<std::vector<mu2e::LoopHelixInfo>>* lhs;
    trkana->SetBranchAddress("demlh", &lhs);
    
    std::vector<std::vector<mu2e::SimInfo>>* sims;
    trkana->SetBranchAddress("demmcsim", &sims);
    
    TH1F* hist_mom1 = new TH1F("hist_mom1","",100, mom_low, 110);
    double nCE = 0;
    double nDIO = 0;
    double nCosmics = 0;
    double nRPC = 0;
    
    unsigned int n_events = trkana->GetEntries();
    for (unsigned int i_event = 0; i_event < n_events; ++i_event) {
      bool passCE = false;
      bool passDIO = false;
      
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
              if (std::fabs(crvcoinc_time - track_time) < 150) { //TODO optimize!!!!
                crvhit = true;
              }
            }
            if (!crvhit and passes_lhcuts) {
              for (auto& sim : *sims) {
                for (auto& s : sim){
                  double startCode = s.startCode;
                  if(fit.mom.R() > mom_low and startCode == 166 and !passDIO ) { nDIO+=1; passDIO=true;}
                  if(fit.mom.R() > mom_low and fit.mom.R() < mom_hi and startCode == 167 and !passCE) { nCE +=1;passCE=true;}
                }
              }
              hist_mom1->Fill(fit.mom.R());
              
            }
          }
        }
      }
    }
    mcresults = make_tuple(nCE,nDIO,nCosmics,nRPC);
    std::cout<<"MC Truth Count: nCE "<<nCE<<" nDIO "<<nDIO<<std::endl;
    return hist_mom1;
}

void RunBinnedFit(TH1F* histmom, TString Run, bool cuts, double mom_lo, double mom_hi, std::tuple <double, double, double, double> &fitresult){
  std::cout<<" ------  calling root-fitter with binned fit -----  "<<std::endl;
  Likelihood *lh = new Likelihood();
  RooFitResult *result = lh->CalculateBinnedLikelihood(histmom, Run, cuts, mom_lo, mom_hi, fitresult);
  result->Print();
}

void RunUnbinnedFit(TTree* mom, TString Run, bool cuts, double mom_lo, double mom_hi, std::tuple <double, double, double, double> &fitresult){
  std::cout<<" ------  calling root-fitter with unbinned fit ----- "<<std::endl;
  Likelihood *lh = new Likelihood();
  RooFitResult *result = lh->CalculateUnbinnedLikelihood(mom, Run, cuts, mom_lo, mom_hi, fitresult);
  result->Print();
}

int main(int argc, char* argv[]){
  std::cout<<"========== Welcome to Mu2e's Reference Ana =========="<<std::endl;
  std::cout<<"----------------Analyzing "<<argv[2]<<" ------------"<<std::endl;

  TString filename = argv[1]; // TrkAna NTuple
  TString runname = argv[2]; // e.g. pass0a
  bool usecuts = argv[3]; //true or false
  TString type = argv[4]; //binned or unbinned
  double mom_lo = 95; 
  double mom_hi = 106;
  
  std::tuple <double, double, double, double> mcresult;
  std::tuple <double, double, double, double> fitresult;
  
  TTree *trkana = ImportNTuple(filename);

  if(type == "binned"){
    TH1F *histmom = make_CRV_cuts(trkana, usecuts, mom_lo, mom_hi, mcresult);
    RunBinnedFit(histmom, runname, usecuts, mom_lo, mom_hi, fitresult);
  } else if (type == "unbinned") {
    TTree *mom = make_CRV_cuts_tree(trkana, usecuts, mom_lo, mom_hi, mcresult);
    RunUnbinnedFit(mom, runname, usecuts, mom_lo, mom_hi, fitresult);
  } else {
    std::cout<<"incorrect fit type, please select binned or unbinned"<<std::endl;
  }
  
  std::cout<<"Fit results NSig = "<<get<0>(fitresult)<<" NDIO = "<<get<1>(fitresult)<<" NCOSMIC = "<<get<2>(fitresult)<<" NRPC = "<<get<3>(fitresult)<<std::endl;
  std::cout<<"MC results NSig "<<get<0>(mcresult)<<" NDIO = "<<get<1>(mcresult)<<" NCOSMIC = "<<get<2>(mcresult)<<" NRPC = "<<get<3>(mcresult)<<std::endl;
  return 0;
}
