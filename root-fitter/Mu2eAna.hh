
#ifndef _Mu2eAna_HH
#define _Mu2eAna_HH

#include <TROOT.h>
#include <TFile.h>
#include <TTree.h>

#include "Likelihood.hh"

using namespace std;

class Mu2eAna  {
  public:
    explicit Mu2eAna(){};
    virtual ~Mu2eAna() = default;
    #ifndef __CINT__
    int main(int argc, char* argv[]);
    TTree *ImportNTuple(TString filename);
    TH1F *GetRecoHist(TTree* trkana, bool usecuts);
    TH1F* make_CRV_cuts(TTree *trkana);
    void RunFit(TString File, TString Run, bool cuts);
    #endif
    ClassDef(Mu2eAna, 0);
};

#endif /* Mu2eAna.hh */
