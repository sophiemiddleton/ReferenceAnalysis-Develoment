#ifndef _Likelihood_hh
#define _Likelihood_hh


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
#include "RooUniform.h"
#include "RooMinimizer.h"
#include "RooAbsReal.h"
//My stuff
#include "ReferenceAna/inc/RooPol58.hh"

#include<tuple>
using namespace std;
using namespace TMath;
using namespace RooFit;
namespace rootfitter{
  class Likelihood  {
      public:
        explicit Likelihood(){};
        explicit Likelihood(const Likelihood &){};
        Likelihood& operator = (const Likelihood &);
        virtual ~Likelihood() = default;
        #ifndef __CINT__
        TString GetLabel(TString run);
        std::tuple <RooRealVar, RooRealVar, RooRealVar, RooRealVar>  CE_parameters();
        std::tuple <RooRealVar, RooRealVar, RooRealVar, RooRealVar>  DIO_parameters();
        void MakePlots(RooRealVar recomom, RooDataHist chMom, RooAddPdf fitFun, TString tag, TString recocuts);
        RooFitResult *CalculateBinnedLikelihood(TH1F *hist_mom1, TString runname, bool usecuts);
        void MakeProfileLikelihood(RooAddPdf fitFun,RooDataHist chMom, RooRealVar nsig, RooRealVar recomom);
        void CalculateUnbinnedLikelihood(TTree *mom, TString runname, bool usecuts);
        #endif
        ClassDef (Likelihood,1);

    };
}
#endif /* Likelihood.hh */
