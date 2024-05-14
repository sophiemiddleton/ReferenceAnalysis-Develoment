# implements chosen set of cuts
# date: 2024

import sys

class Cuts() :

    def __init__(self, opt = 'su2020', use_CRV = False): #default is su2020
        self.use_CRV = use_CRV
        self.Cut_List = {}

        if opt is 'su2020':
                self.Cut_List =  {
                      "de.t0" : [700., 1695],    #inTimeWindow
                      "deent.td" : [0.5, 1.0],    #inTanDipCut
                      "deent.d0" : [-100,100.], #inD0Cut
                      "dequal.TrkQual" : [0.2, float("inf")],  #TrkQual
                    }

    def ApplyCut(self, df):
        df_cut = df
        for key, value in self.Cut_List.items():
            df_cut = df_cut[(df_cut[key] > value[0]) & (df_cut[key] <= value[1])]
        return df_cut
