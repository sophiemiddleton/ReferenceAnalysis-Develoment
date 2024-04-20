#!/usr/bin/python
# Author: S Middleton
# Date: 2020
# Purpose: Import Data to StatsTool

import uproot
import sys
import argparse
import math
from optparse import OptionParser
import matplotlib.pyplot as plt
from ImportRecoData import ImportRecoData
from ImportGenData import ImportGenData
from Histograms import Histograms
from Mu2eNegFunctions import *
from Constants import *
from Results import Results


def main(options, args):
    print("=====================================================================")
    print("=====================================================================")
    print("=================== Mu2e Cut-and-count Analysis =====================")
    print("=====================Written by S. Middleton=========================")
    print("=========================smidd@caltech.edu===========================")
    print("=====================================================================")
    print("Users Options: CE", options.filename, options.treename, options.branchname)
    print("===================calculating stats....please wait....==============")

    # Pandas offers the most flexible analysis - arguments are used for window optimization only:
    Run(100, options.mom_low, options.mom_high)
    # TODO- add a UseROOT version

def Run(nbins, mom_low, mom_high,):

    # Import the data into panadas dataframes:
    recodata = ImportRecoData(options.filename, options.treename, otions.branchname)

    # Make list of ROOT histograms for analysis (this step should be removed)
    histos = Histograms(nbins, mom_low, mom_high,)

    # Fille Reco dataframs (Note last arguement sets DoCuts - look at cuts.py for options)
    DIO_reco_mom = recodata.GetFeature( "DIO", "deent.mom",False,True)
    CE_reco_mom = recodata.GetFeature( "signal", "deent.mom",False,True)

    # Fill Reco Hists:
    histos.FillHistogram(histos.histo_CE_reconstructed , CE_reco_mom)
    histos.FillHistogram(histos.histo_DIO_reconstructed_flat , DIO_reco_mom)

    histos.DoDIOWeights(histos.histo_DIO_reconstructed_reweighted , DIO_reco_mom)

    # Fill Generation dataframs:
    DIO_gen_mom = gendata.GetFeature("DIO", "TMom")
    CE_gen_mom = gendata.GetFeature("signal", "TMom")

    # Fill Gen Hists:
    histos.FillHistogram(histos.histo_CE_generated , CE_gen_mom)
    histos.FillHistogram(histos.histo_DIO_generated_flat , DIO_gen_mom)

    histos.DoDIOWeights(histos.histo_DIO_generated_reweighted , DIO_gen_mom)

    # Import constants - this is were we store nPOT, capture/decay rates etc.
    # Edit the constants if you have a new design to reflect that.
    constants = Constants()

    # Build Mu2e yields Functions:
    yields = YieldFunctions(mom_low, mom_high, constants)

    # Fill Results i.e. optimial window (requires work)
    yields.FillResults()

    # Get SES/BFUL/Eff for fixed signal window:
    yields.GetSingleResult(constants.fixed_window_lower, constants.fixed_window_upper)

    # Save plots:
    yields.WriteHistograms()

if __name__ == "__main__":

    parser = OptionParser()

    # example use: python main.py --filelist "trkana7.root" --treename "TrkAnaNeg" --branchname "trkana"
    parser.add_option('-b', action='store_true', dest='noX', default=False, help='no X11 windows')
    parser.add_option('-f','--filelist', dest='filelist', default = 'trkana7.root',help='filelist', metavar='fdir')
    parser.add_option('-t','--treename', dest='treename', default = 'TrkAnaNeg',help='treename', metavar='tdir')
    parser.add_option('-n','--branchname', dest='branchname', default = 'trkana', help='branchname', metavar='bdir')
    parser.add_option('-l','--mom_low', dest='mom_low', default = '95', help='mom_low', metavar='ldir')
    parser.add_option('-g','--mom_hi', dest='mom_hi', default = '115', help='mom_hi', metavar='hdir')

    (options, args) = parser.parse_args()

    main(options, args)
