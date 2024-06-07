


import numpy as np


class Cuts() :

    def __init__(self, opt = 'su2020', use_CRV = False): #default is su2020
        self.use_CRV = use_CRV
        self.Cut_List = {}

        if opt=='su2020':
                self.Cut_List =  {
                      "de.t0" : [700., 1695],    #inTimeWindow
                      "deent.td" : [0.5, 1.0],    #inTanDipCut
                      "deent.d0" : [-100,100.], #inD0Cut
                      "dequal.TrkQual" : [0.2, float("inf")],  #TrkQual
                    }
        if opt=='testing':
            # cuts applied to parameters at start of tracker (demfit sid = 0)
            self.cutsdict =  {
                # signal momentum window from SU2020 Universe report
                'demfit_mom0' : [103.6,104.9],
                # signal window start and end times
                'demfit_t0' : [640, 1650], 
                # maximum radius range
                'demlh_maxr0' : [450,680],
                # implement additional cuts
                # 
            }

    def ApplyCut(self, df):
        df_cut = df
        for key, value in self.Cut_List.items():
            df_cut = df_cut[(df_cut[key] > value[0]) & (df_cut[key] <= value[1])]
        return df_cut

    def apply_cuts_indicator(self,data):
        """ Add indicator showing which entries pass cut. No entries are actually removed here. """
        for key,value in self.cutsdict.items():
            #print(key,value)
            keycut = key+'_cut'
            if np.size(value)==1: # single value to match
                data[keycut] = data[key]==value
            else: # upper and lower limits
                data[keycut] = (data[key]>value[0]) & (data[key]<value[1])
        return data



