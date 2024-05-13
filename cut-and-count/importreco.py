# imports NTupled data from reconstructed data/MC
# date: 2024

import awkward as ak
import sys
import uproot
import pandas
import math
import numpy as np
import matplotlib.pyplot as plt
from cuts import *

class ImportRecoData :

    def __init__(self, fileName, treeName = "TrkAna", branchName = "trkana"):
        """ Initialise the Class Object """
        self.fileName = fileName
        self.treeName = treeName
        self.branchName = branchName
        self.cuts = Cuts()

    def Import_RecoFits(self, leafname, leafname_field):
        """ import reconstructed trk ana"""
        # import with uproot
        trkana = uproot.open(self.fileName+":"+str(self.treeName)+"/"+str(self.branchName))
        # find track fit branches for downstream (d) electron (em) loop helix (lh):
        branches = trkana.arrays(filter_name=["/"+str(leafname)+"/", "/"+str(leafname_field)+"/"])
        return branches

    def Count(self, branches, low, hi, time):
        """ count events in described window """
        branches['demfit_mom'] = np.sqrt((branches['demfit']['mom']['fCoordinates']['fX'])**2 + (branches['demfit']['mom']['fCoordinates']['fY'])**2 + (branches['demfit']['mom']['fCoordinates']['fZ'])**2)
        
        # find entrance
        trk_mask = (branches['demlh']['t0']>=float(time) )
        #### TODO - count events in given signal region ####
        return len(trk_mask)
        
        

    def PlotRecoMom(self, branches, low, hi, time):
        """ make basic reco mom plot, no position requirement """
        branches['demfit_mom'] = np.sqrt((branches['demfit']['mom']['fCoordinates']['fX'])**2 + (branches['demfit']['mom']['fCoordinates']['fY'])**2 + (branches['demfit']['mom']['fCoordinates']['fZ'])**2)
        fig, ax = plt.subplots(1,1)
        n, bins, patches = ax.hist(ak.flatten(branches['demfit_mom'], axis=None), bins=50, range=(int(low), int(hi)), label='pass0a', histtype='step',color='b')
        bin_centers = 0.5 * (bins[:-1] + bins[1:])
        yerrs = []
        for i, j in enumerate(n):
          yerrs.append(math.sqrt(j))
        plt.errorbar(bin_centers, n, yerr=np.sqrt(n), fmt='b.')
        # add in style features:
        ax.set_yscale('log')
        ax.set_xlabel('Reconstructed Momentum (demfit_mom all) [MeV/c]')
        ax.set_ylabel('Entries per bin')
        ax.grid(True)
        ax.legend()
        plt.show()
       
    def PlotRecoMomEnt(self, branches, low, hi, time):
        """ make basic reco mom plot, requirement for tracker entrance """
        branches['demfit_mom'] = np.sqrt((branches['demfit']['mom']['fCoordinates']['fX'])**2 + (branches['demfit']['mom']['fCoordinates']['fY'])**2 + (branches['demfit']['mom']['fCoordinates']['fZ'])**2)
        trk_ent_mask = (branches['demfit']['sid']==0)
        
        fig, ax = plt.subplots(1,1)
        nEnt, binsEnt, patchesEnt = ax.hist(ak.flatten(branches[(trk_ent_mask)]['demfit_mom'], axis=None), bins=100, range=(int(low), int(hi)), label='ent fits', histtype='step',color='g')

        bin_centersEnt = 0.5 * (binsEnt[:-1] + binsEnt[1:])
        yerrsEnt = []
        for i, j in enumerate(nEnt):
          yerrsEnt.append(math.sqrt(j))
        plt.errorbar(bin_centersEnt, nEnt, yerr=np.sqrt(nEnt), fmt='g.')

        # add in style features:
        ax.set_yscale('log')
        ax.set_xlabel('Reconstructed Momentum (demfit_mom at ent) [MeV/c]')
        ax.set_ylabel('Entries per bin')
        ax.grid(True)
        ax.legend()
        plt.show()
        
