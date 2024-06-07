

import numpy as np


   
def apply_cuts(data,cutsdict):
    # add indicator showing which entries pass cut
    for key,value in cutsdict.items():
        #print(key,value)
        keycut = key+'_cut'
        if np.size(value)==1: # single value to match
            data[keycut] = data[key]==value
        else: # upper and lower limits
            data[keycut] = (data[key]>value[0]) & (data[key]<value[1])
    return data


def preprocessing1(branches):
    # only looking at events with one reconstructed track
    branches['ntrk'] = [len(p) for p in branches['demfit']['sid']]
    branches = apply_cuts(branches, {'ntrk' : 1})
    branches = branches[branches['ntrk_cut']]
    
    # reconstructed track momentum (start, middle, end of tracker)
    branches['demfit_mom'] = np.sqrt((branches['demfit']['mom']['fCoordinates']['fX'])**2 +
                                 (branches['demfit']['mom']['fCoordinates']['fY'])**2 + 
                                 (branches['demfit']['mom']['fCoordinates']['fZ'])**2)
    # reconstructed momentum at start of tracker
    branches['demfit_mom0'] = branches['demfit_mom'][branches['demfit','sid']==0]
    # time from demfit at start of tracker
    branches['demfit_t0'] = branches['demfit','time'][branches['demfit','sid']==0]
    # maximum radius from demlh at start of tracker
    branches['demlh_maxr0'] = branches['demlh','maxr'][branches['demfit','sid']==0]

    # first process for each event is CE or DIO in this data sample
    branches['mcproc1'] = branches['demmcsim','startCode'][:,0,0]
    
    return branches







