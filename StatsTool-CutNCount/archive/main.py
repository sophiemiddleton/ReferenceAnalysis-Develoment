#!/usr/bin/python
# Author: S Middleton
# Date: 2020
# Purpose: Import Data to StatsTool

import uproot
import sys
import argparse
import math
from importreco import ImportRecoData

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
    branches = recodata.Import_branches("demfit", "demlh")
    # make a histogram of this:
    recodata.PlotRecoMom(branches, options.mom_low, options.mom_hi, options.time_low)
    recodata.PlotRecoMomEnt(branches, options.mom_low, options.mom_hi, options.time_low)
    # count number of events in the chosen window
    count_time = recodata.Count(branches, options.mom_low, options.mom_hi, options.time_low)
    print(count_time)
    
if __name__ == "__main__":

    parser = OptionParser()

    if __name__ == "__main__":
    # example use: python main.py --filelist "<filename>.root" --treename "TrkAna" --branchname "trkana" --fit_range_low 95 --fit_range_hi 115 
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", default="nts.mu2e.trkana-reco-CE-DIO-1month.MDC2020ad_perfect_v1_2.0.tka", help="filename")
    parser.add_argument("--treename", default="TrkAna", help="treename")
    parser.add_argument("--branchname", default="trkana", help="branchname")
    parser.add_argument("--fitrange_mom_low", default=95, help="fitrange_mom_low")
    parser.add_argument("--fitrange_mom_hi", default=115, help="fitrange_mom_hi")
    parser.add_argument("--verbose", default=0, help="verbose")
    args = parser.parse_args()
    (args) = parser.parse_args()
    main(args)
