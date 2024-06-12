

import numpy as np
import awkward as ak

   
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


def preprocessing1(branches,use_crv=False):
    # only looking at events with one reconstructed track
    branches['ntrk'] = [len(p) for p in branches['demfit']['sid']]
    branches = apply_cuts(branches, {'ntrk' : 1})
    branches = branches[branches['ntrk_cut']]
    # skip events with missing reconstructed momentum components (nan track quality)
    branches = branches[~np.isnan(branches['result'])]
    
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
    # track quality # find a way to rename in place
    branches['demtrkqual_result'] = branches['result']
    # CRV time difference
    if use_crv:
        branches['crv_timediff'] = branches['demfit_t0'] - ak.max(branches['crvcoincs.time'],axis=-1)
        # filling none entries with large time diff as placeholder
        branches['crv_timediff']=ak.fill_none(branches['crv_timediff'],[[1e6]],axis=0)
     
    # first process for each event
    branches['mcproc1'] = branches['demmcsim','startCode'][:,0,0]
    
    return branches







