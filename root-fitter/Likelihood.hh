#ifndef _Likelihood_HH
#define _Likelihood_HH


#include <fstream>
#include <iostream>
#include "TSystem.h"
#include "TROOT.h"
#include "TStyle.h"
#include "TFile.h"
#include "TH1.h"

#include "TF1.h"
#include "TMath.h"
#include "TTree.h"
#include "TCanvas.h"
#include "TPad.h"
#include "TMath.h"
#include <Riostream.h>

#include "TPaveStats.h"
#include "TPaveText.h"
#include "TLatex.h"
#include "TLegend.h"
#include "TPaveLabel.h"
#include "TAttFill.h"
// add roofit header files
#include "RooHist.h"
#include "RooRealVar.h"
#include "RooPlot.h"
#include "RooDataSet.h"
#include "RooDataHist.h"
#include "RooKeysPdf.h"
#include "RooHistPdf.h"
#include "RooGaussian.h"
#include "RooAddPdf.h"
#include "RooArgList.h"
#include "RooCBShape.h"
#include "RooGenericPdf.h"
#include "RooFFTConvPdf.h"
#include "RooFitResult.h"

//My stuff
#include "RooPol58.hh"
//#include "RooCeMLL.hh"

using namespace std;
using namespace TMath;
using namespace RooFit;

using namespace std;

class Likelihood  {
  public:
    #ifndef __CINT__
    explicit Likelihood(){};
    Likelihood(const Likelihood &);
    Likelihood& operator=(const Likelihood &);
    virtual ~Likelihood() = default;
    TString GetLabel(TString run);
    void MakePlots(RooRealVar recomom, RooDataHist chMom, RooAddPdf fitFun, TString tag, TString recocuts);
    RooFitResult *CalculateLikelihood(TH1F *hist_mom1, TString runname, bool usecuts);
    #endif
    ClassDef (Likelihood,0);

};

#endif /* Likelihood.hh */
