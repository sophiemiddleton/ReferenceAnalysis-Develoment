#include "Likelihood.hh"
ClassImp(Likelihood);

/*Gaussian Likelihood::MakeGaussianNusiance(std::string name, double mean, double sigma) const{
  Gaussian g(name, mean, sigma);
  return g;
}*/


TString Likelihood::GetLabel(TString run){
  TString pass;
  if (run == "pass0a"){
      pass = "CE-DIO(p>95MeV/c)-MixBB-1month";
  }
  else if (run == "pass0b"){
      pass = "CE-DIO(p>95MeV/c)-CRY-1BB-1week";
  } else {
      pass = "unknown";
  }
  return pass;
}

void Likelihood::MakePlots(RooRealVar recomom, RooDataHist chMom, RooAddPdf fitFun, TString tag, TString recocuts){
    TCanvas *can = new TCanvas("can", "", 100, 100, 600, 600);

    RooPlot *chFrame = recomom.frame(Title(""));
    chMom.plotOn(chFrame, MarkerColor(kBlack), LineColor(kBlack), MarkerSize(0.5), Name("chMom"));

    //Sig.plotOn(chFrame, LineColor(kRed), LineStyle(1), Name("sig"));
    //DIO.plotOn(chFrame, LineColor(kBlue), LineStyle(1), Name("dio"));
    fitFun.plotOn(chFrame, LineColor(kGreen), LineStyle(1), Name("combFit"));

    float chiSq = chFrame->chiSquare(11);
    std::cout << "chi2: " << chiSq << "; Probability: " << Prob(chiSq, 151) << std::endl;
    TPaveLabel *pchi2 = new TPaveLabel(0.5, 0.70, 0.35, 0.80, Form("#chi^{2}/ndf = %4.2f", chiSq), "brNDC");
    pchi2 -> SetFillStyle(0);
    pchi2 -> SetBorderSize(0);
    pchi2 -> SetTextSize(0.25);
    pchi2 -> SetTextColor(kBlack);
    pchi2 -> SetFillColor(kWhite);
    chFrame -> addObject(pchi2);
    auto *th1 = new TLatex(105 - 1, 100,"Mu2e Mock Data 2024");
    th1->SetTextAlign(31); 
    th1->SetTextSize(0.05);
    auto *th2 = new TLatex(105 - 1 , 50, tag);
    th2->SetTextAlign(31); 
    th2->SetTextSize(0.03);
    auto *th3 = new TLatex(105 - 1 , 20, recocuts);
    th3->SetTextAlign(31); 
    th3->SetTextSize(0.03);

    chFrame -> SetYTitle("Events per 25 keV");
    chFrame -> SetYTitle("Reconstructed Mom at TrkEnt [MeV/c]");
    can -> Draw();
    chFrame -> Draw("same");
    th1->Draw("same");
    th2->Draw("same");
    th3->Draw("same");
    can -> SetLogy();
    can -> Update();
    can -> SaveAs("CombinedFitResult.root");
}

std::tuple <RooRealVar, RooRealVar, RooRealVar, RooRealVar>  Likelihood::CE_parameters(){
    // CE parameters (assume simple crystal ball for now)
    RooRealVar fMean("mean", "mean", 104, 103, 105);
    RooRealVar fWidth("sigma", "sigma", 0.5, 0.1, 1.0);
    RooRealVar fcbalpha("fcbalpha", "fcbalpha", 2.5, 0.05, 20.0);
    RooRealVar fcbndeg("fcbndeg", "fcbndeg", 10., 0.25, 80.);
    std::tuple <RooRealVar, RooRealVar, RooRealVar, RooRealVar> par_tuple = make_tuple(fMean,fWidth,fcbalpha,fcbndeg);
    return par_tuple;
}

std::tuple <RooRealVar, RooRealVar, RooRealVar, RooRealVar>  Likelihood::DIO_parameters(){
    RooRealVar a5("a5", "a5", 8.6434e-17, 8.5e-17, 8.7e-17);
    RooRealVar a6("a6", "a6", 1.16874e-17, 1.1e-17, 1.2e-17);
    RooRealVar a7("a7", "a7", -1.87828e-19, -1.9e-19, -1.8e-19);
    RooRealVar a8("a8", "a8", 9.16327e-20, 9.1e-20, 9.2e-20);
    std::tuple <RooRealVar, RooRealVar, RooRealVar, RooRealVar> par_tuple = make_tuple(a5,a6,a7,a8);
    return par_tuple;
    
    
}

RooFitResult *Likelihood::CalculateLikelihood(TH1F *hist_mom1, TString runname, bool usecuts)
{
    TString recocuts = "";

    if(usecuts){
      recocuts = "demfit.sid==0 && demlh.t0 > 700 && demlh.t0err < 0.9 && demtrkqual.result > 0.2 && dem.nactive > 20 && demlh.maxr < 680";
    }
    TString tag = GetLabel(runname);
    
    // make RooFit objects
    RooRealVar recomom("recomom", "reco mom [MeV/c]", 95, 105); //TODO - should make these input parameters
    RooDataHist chMom("chMom", "chMom", recomom, hist_mom1);

    // CE signal shape:
    std::tuple <RooRealVar, RooRealVar, RooRealVar, RooRealVar> CEparams = CE_parameters();
    RooCBShape Sig("Sig", "signal peak", recomom, get<0>(CEparams), get<1>(CEparams),get<2>(CEparams),get<3>(CEparams));
    RooRealVar nsig("nsig", "number of signal events", 0.0, 0.0, 100);
   
    // DIO shape:
    std::tuple <RooRealVar, RooRealVar, RooRealVar, RooRealVar> DIOparams = DIO_parameters();
    RooRealVar ndio("ndio", "number in dio region", 0.0, 0.0, 100000);
    RooPol58 DIO("DIO", "dio tail", recomom, get<0>(DIOparams), get<1>(DIOparams),get<2>(DIOparams),get<3>(DIOparams));
    
    //combined binned ML (extended)
    RooAddPdf fitFun("fitFun", "Sig + DIO", RooArgList(Sig,DIO), RooArgList(nsig, ndio));
    RooFitResult *fitRes = fitFun.chi2FitTo(chMom, Range(95, 105), Strategy(3), PrintLevel(1), Hesse(kTRUE), Extended(), Save());
    
    MakePlots(recomom, chMom, fitFun, tag, recocuts);
    return fitRes;
}
