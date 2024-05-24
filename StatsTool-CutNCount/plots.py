

import numpy as np
import matplotlib.pyplot as plt
import awkward as ak


def bin_errorbars(ax,n,bins,color):
    bin_centers = 0.5 * (bins[:-1] + bins[1:])
    yerrs = []
    for i, j in enumerate(n):
      yerrs.append(np.sqrt(j))
    ax.errorbar(bin_centers, n, yerr=np.sqrt(n), fmt=color+'.')
    


# will be updated to include additional cuts and fewer hardcoded parameters
def PlotRecoMomEnt2(branches, low, hi,labels,plots,cuts_legend):
    """ visualize results of cut and count """
    fig, axs = plt.subplots(1,2,width_ratios=(3,1),figsize=(8,4))
    colors = dict(zip(plots,['b','g']))
    # events in signal window
    n, bins, patches = axs[0].hist(ak.flatten(branches['demfit_mom0'][~branches['demfit_mom0_cut']], axis=None), 
                                        bins=100, range=(int(low), int(hi)), 
                                        label=labels['sig'], color=colors['sig'],
                                        histtype='step',)
    # events outside signal window
    n2, bins2, patches2 = axs[0].hist(ak.flatten(branches['demfit_mom0'][branches['demfit_mom0_cut']], axis=None),
                                        bins=100, range=(int(low), int(hi)), 
                                        label=labels['other'], color=colors['other'],
                                        histtype='step',)
    # sqrt(n) error bars
    bin_errorbars(axs[0],n,bins,color=colors['sig'])
    bin_errorbars(axs[0],n2,bins2,color=colors['other'])
    
    # add in style features:
    axs[0].set_title('Cut and Count with SU2020 Parameters')
    axs[0].set_yscale('log')
    axs[0].set_xlabel('Reconstructed Momentum at Tracker Entrance [MeV/c]')
    axs[0].set_ylabel('Entries per bin')
    axs[0].grid(True)
    axs[0].legend()
    # second axis for cuts legend. placeholder for listing more cuts
    axs[1].set_axis_off()
    axs[1].text(0,0.95,'Cuts Applied')
    for i,s in enumerate(cuts_legend):
        offset=0.18*(i+1)
        axs[1].text(0,1-offset,s[0])
        axs[1].text(0,1-offset-0.06,s[1])
        
    plt.show()





