/*
File sets a standard plot style
*/
#include "TStyle.h"
#include "TROOT.h"
void StyleSetting(){

      TStyle *MyStyle = new TStyle("myStyle","My style");
      Int_t icol=0;

      MyStyle->SetFrameBorderMode(icol);
      MyStyle->SetFrameFillColor(icol);
      MyStyle->SetCanvasBorderMode(icol);
      MyStyle->SetCanvasColor(icol);
      MyStyle->SetPadBorderMode(icol);
      MyStyle->SetPadColor(icol);
      MyStyle->SetStatColor(icol);
      //MyStyle->SetPaperSize(20,26);

      MyStyle->SetPadTopMargin(0.05);
      MyStyle->SetPadRightMargin(0.05);
      MyStyle->SetPadBottomMargin(0.16);
      MyStyle->SetPadLeftMargin(0.16);

      MyStyle->SetTitleXOffset(0.8);
      MyStyle->SetTitleYOffset(0.8);

      Style_t font=42;
      Double_t tsize=0.04;
      MyStyle->SetTextFont(font);
      MyStyle->SetTextSize(tsize);
      MyStyle->SetLabelFont(font,"XYZ");
      MyStyle->SetTitleFont(font,"XYZ");

      MyStyle->SetLabelSize(tsize,"XYZ");
      MyStyle->SetTitleSize(0.06,"XYZ");


      MyStyle->SetLegendBorderSize(0);
      MyStyle->SetLegendTextSize(0.03);
      MyStyle->SetLineStyleString(2,"[12 12]");

      MyStyle->SetEndErrorSize(0.);

      MyStyle->SetOptTitle(0);
      MyStyle->SetOptStat("MR");
      MyStyle->SetOptStat(0);
      MyStyle->SetOptFit(0);

      MyStyle->SetPadTickX(1);
      MyStyle->SetPadTickY(1);

      //MyStyle->SetHistLineWidth(2);
      MyStyle->SetLineWidth(3);

      MyStyle->SetHistLineWidth(3);
      MyStyle->SetHistLineColor(kBlack);

      MyStyle->SetPalette(8,nullptr);

      MyStyle->SetFuncWidth(3);
      MyStyle->SetFuncColor(kGreen);

      MyStyle->cd();
      gROOT->ForceStyle();
      MyStyle->ls();

  }
