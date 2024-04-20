# Author : S Middleton
# Date : 2020
# Purpose : class to store histograms
#TODO - this class requires work!

import sys
import ROOT
from ROOT import TMath, TH1F, TTree, TBranch
import numpy as np
class Histograms :
    def __init__(self, nBins, momentum_lower_limit, momentum_upper_limit, target_mass_scalefactor=1):

        self.histo_CE_reconstructed = TH1F("Reconstructed CE","Reconstructed CE",nBins,momentum_lower_limit,momentum_upper_limit)
        self.histo_CE_generated = TH1F("Generated CE","Generated CE",nBins,momentum_lower_limit,momentum_upper_limit)

        self.histo_DIO_reconstructed_reweighted = TH1F("Reconstructed DIO_reweighted","Reconstructed DIO_reweighted",nBins,momentum_lower_limit,momentum_upper_limit)
        self.histo_DIO_generated_reweighted = TH1F("Generated DIO_reweighted","Generated DIO_reweighted",nBins,momentum_lower_limit,momentum_upper_limit)

        #self.histo_Cosmics_reconstructed = TH1F("histo_Cosmics_reconstructed","histo_Cosmics_reconstructed",nBins,momentum_lower_limit,momentum_upper_limit)
        #self.histo_Cosmics_generated = TH1F("histo_Cosmics_generated","histo_Cosmics_generated",nBins,momentum_lower_limit,momentum_upper_limit)

        self.histo_CE_reconstructed.Sumw2()
        self.histo_CE_generated.Sumw2()
        self.histo_DIO_reconstructed_reweighted.Sumw2()
        self.histo_DIO_generated_reweighted.Sumw2()

    def FillHistogram(self, histogram, data):
        for i, j in enumerate(data):
            histogram.Fill(j)
        return histogram

    """
    def DoDIOWeights(self, histogram, data):
        dio = DIO()
        for i, j in enumerate(data):
            dio_weight =  dio.DIOWeight(j)
            histogram.Fill(j, dio_weight / 7.91001e-10 )
    """
