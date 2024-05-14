# Author : S Middleton
# Date : 2020
# Purpose : Stats functions

import sys
import math
import numpy
import ROOT
from ROOT import TMath, TH1F, TF1, TCanvas
from Histograms import Histograms
from Results import Results
from DIO import DIO
from StatsFunctions import *
from Constants import *

class YieldFunctions:

        def __init__(self,histos, nbins, mom_low, mom_high,constants):
            self.optimize_for = 'BFUL'
            self.momentum_lower_limit = mom_low
            self.momentum_upper_limit = mom_high
            self.nBins = nbins
            self.momentum_Bin_width = (mom_high - mom_low)/nbins
            self.constants = constants
            self.Histos = histos
            self.Results = []
            self.DIO = DIO()
            self.CE = CE()

        def MomLowLimit(self):
            return self.momentum_lower_limit

        def MomHighLimit(self):
            return self.momentum_upper_limit

        def NBins(self):
            return self.nBins

        def NBins(self):
            return (self.MomHighLimit()-self.MomLowLimit())/self.NBins()

        def MomBinWidth(self):
            return self.momentum_Bin_width

        def SignalRegionStart(self):
            return self.constants.signal_start

        def SignalRegionEnd(self):
            return self.constants.signal_end

        def GetPOT(self):
            return self.constants.POT

        def CapturesPerStop(self):
            return self.constants.capturesperStop

        def DecaysPerStop(self):
            return self.constants.decaysperStop

        def MuonStopsPerPOT(self):
            return self.constants.muonstopsperPOT

        def GetCESimEff(self):
            return self.constants.sim_ce_eff

        def GetDIOSimEff(self):
            return self.constants.sim_dio_eff

        def GetIntegral(self, histo, mom_low, mom_high):
            # Translate mom_low and mom_up in bin numbers
            bin_low = TMath.Nint((mom_low - self.MomLowLimit()) / self.MomBinWidth()) + 1
            bin_high = TMath.Nint((mom_high - self.MomLowLimit()) / self.MomBinWidth()) + 1
            return histo.Integral(bin_low,bin_high)

        def GetN(self, histo, mom_low, mom_high):
            Nrec = self.GetIntegral(histo, mom_low, mom_high)
            return Nrec

        def GetNError(self, histo, mom_low,  mom_high):
            Nrec_error = 0
            # compute error from sum of weigths in the bins
            # translate mom_low and mom_up in bin numbers
            bin_low = TMath.Nint((mom_low - self.MomLowLimit()) / self.MomBinWidth())+1
            bin_high = TMath.Nint((mom_high - self.MomLowLimit()) / self.MomBinWidth())+1
            temp_error_sum = 0
            for i in range(bin_low, bin_high):
                temp_error_sum += pow(histo.GetBinError(i), 2)
            Nrec_error = math.sqrt(temp_error_sum)
            return Nrec_error

        def GetRecoEff(self, Nrec, Ngen, simeff):
            efficiency = (Nrec/simeff) / Ngen
            return efficiency

        def GetRecoEffError(self, Nrec, Ngen):
            """
            use Glen Cowan derivation of efficiency error based on a binomial distribution
            http://www.pp.rhul.ac.uk/~cowan/stat/notes/efferr.pdf
            """
            efficiency_error = math.sqrt(Nrec * (1. - Nrec/Ngen)) / Ngen
            return efficiency_error

        def GetDIOEffError(self, Nrec, Nrec_error, Ngen, Ngen_error):
            efficiency_error = math.sqrt( pow(Nrec_error / Ngen, 2) + pow( Nrec * Ngen_error / (Ngen*Ngen), 2) )
            return efficiency_error

        def GetSignalExpectedYield(self, efficiency_CE):
            # assume BF of 10E-16 and calculate expected signal for this BF
            BF_assumption = 1e-16
            N_CE_expected = self.GetPOT() * self.MuonStopsPerPOT() * self.CapturesPerStop() * BF_assumption * efficiency_CE
            return N_CE_expected

        def GetSES(self, efficiency_CE):
            # calculate single event sensitivity (SES), corresponds to branching fraction where 1 signal event is observed
            SES = 1. / ( self.GetPOT() * self.MuonStopsPerPOT() * self.CapturesPerStop() * efficiency_CE  )
            return SES

        def GetSESError(self, efficiency_CE, efficiency_error_CE):
            # calculate error of single event sensitivity (SES),
            #corresponds to uncertainting on branching fraction where 1 signal event is observed
            SES = 1. / ( self.GetPOT() * self.MuonStopsPerPOT() * self.CapturesPerStop() * pow(efficiency_CE, 2) ) * efficiency_error_CE  # error propagation on SES calculation
            return SES

        def GetDIOExpectedYield(self, N_DIO_rec, N_DIO_gen, efficiency_error_DIO, mom_low, mom_high):
            CzerneckiIntegral = self.DIO.GetInt(mom_low, mom_high,self.constants.target)
            N_DIO_expected = N_DIO_rec * CzerneckiIntegral * self.GetPOT() * self.MuonStopsPerPOT() * self.DecaysPerStop() / N_DIO_gen
            N_DIO_expected_error = CzerneckiIntegral * self.GetPOT() * self.MuonStopsPerPOT() * self.DecaysPerStop() * efficiency_error_DIO
            return N_DIO_expected, N_DIO_expected_error

        def GetCosmicsExpectedYield(self, eff):
            return 0., 0.

        def GetBFUL(self, Nsig_UL, efficiency_CE):
            BF_upper_limit = Nsig_UL / ( self.GetPOT() * self.MuonStopsPerPOT() * self.CapturesPerStop() * efficiency_CE )
            return BF_upper_limit

        def GetBFULError(self, Nsig_UL, Nsig_UL_error, efficiency_CE, efficiency_error_CE):
            BF_upper_limit_error = 1. / (self.GetPOT() * self.MuonStopsPerPOT() * self.CapturesPerStop()) * math.sqrt(pow(Nsig_UL_error/efficiency_CE, 2)
            + pow(Nsig_UL * efficiency_error_CE/(efficiency_CE*efficiency_CE), 2))
            return BF_upper_limit_error

        def GetSingleResult(self, mom_low, mom_high):
            # find optimized window
