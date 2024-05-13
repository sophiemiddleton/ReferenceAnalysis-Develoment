#!/usr/bin/python
# Author: S Middleton
# Date: 2020
# Purpose: Import Data to StatsTool

import uproot
import sys
import argparse
import math
from optparse import OptionParser
from importreco import ImportRecoData
"""
from ImportGenData import ImportGenData
from Histograms import Histograms
from Mu2eNegFunctions import *
from Constants import *
from Results import Results
"""

def main(options, args):
    print("=====================================================================")
    print("=====================================================================")
    print("=================== Mu2e Cut-and-count Analysis =====================")
    print("=================Written by Mu2e Analysis Tools Grp==================")
    print("=========================smidd@caltech.edu===========================")
    print("=====================================================================")
    #print("Users Options:", options.filelist, options.treename, options.branchname)
    print("===================calculating stats....please wait....==============")

    Run()

def Run():
    # Import the data into panadas dataframes:
    recodata = ImportRecoData(options.filelist, options.treename, options.branchname)
    # extract reco mom for Loop Helix:
    branches = recodata.Import_RecoFits("demfit", "demlh")
    # make a histogram of this:
    recodata.PlotRecoMom(branches, options.mom_low, options.mom_hi, options.time_low)
    recodata.PlotRecoMomEnt(branches, options.mom_low, options.mom_hi, options.time_low)
    # count number of events in the chosen window
    count_time = recodata.Count(branches, options.mom_low, options.mom_hi, options.time_low)
    print(count_time)
    
if __name__ == "__main__":

    parser = OptionParser()

    # example use: python main.py --filelist "trkana7.root" --treename "TrkAnaNeg" --branchname "trkana"
    parser.add_option('-b', action='store_true', dest='noX', default=False, help='no X11 windows')
    parser.add_option('-f','--filelist', dest='filelist', default = 'trkana7.root',help='filelist', metavar='fdir')
    parser.add_option('-t','--treename', dest='treename', default = 'TrkAnaNeg',help='treename', metavar='tdir')
    parser.add_option('-n','--branchname', dest='branchname', default = 'trkana', help='branchname', metavar='bdir')
    parser.add_option('-l','--mom_low', dest='mom_low', default = '95', help='mom_low', metavar='ldir')
    parser.add_option('-g','--mom_hi', dest='mom_hi', default = '115', help='mom_hi', metavar='hdir')
    parser.add_option('-a','--time_low', dest='time_low', default = '0', help='time_low', metavar='hdir')
    (options, args) = parser.parse_args()

    main(options, args)
