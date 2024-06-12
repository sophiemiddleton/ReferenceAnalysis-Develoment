

import numpy as np
import matplotlib.pyplot as plt
import awkward as ak


def bin_errorbars(ax,n,bins,color):
    bin_centers = 0.5 * (bins[:-1] + bins[1:])
    yerrs = []
    for i, j in enumerate(n):
      yerrs.append(np.sqrt(j))
    ax.errorbar(bin_centers, n, yerr=np.sqrt(n), fmt=color+'.')
    
def plottable(matrix,rowlabels,collabels):
    fig,ax = plt.subplots()
    table = ax.table(matrix,
                     rowLabels=rowlabels,
                     colLabels=collabels,
                     loc='center');
    plt.subplots_adjust(left=0.3, top=0.3)
    ax.axis("off")
    table.scale(1,6);
    plt.show()


def PlotRecoMomEnt2(branches, low, hi,labels,plots,cuts_legend,cut_results,data_description):
    """ visualize results of cut and count """
    fig, axs = plt.subplots(1,2,width_ratios=(3,1),figsize=(8,4))
    colors = dict(zip(plots,['b','g']))
    # events in signal window
    idx=np.prod(cut_results,axis=0,dtype=bool)
    n, bins, patches = axs[0].hist(ak.flatten(branches['demfit_mom0'][~idx], axis=None), 
                                        bins=100, range=(int(low), int(hi)), 
                                        label=labels['sig'], color=colors['sig'],
                                        histtype='step',)
    # events outside signal window
    n2, bins2, patches2 = axs[0].hist(ak.flatten(branches['demfit_mom0'][idx], axis=None),
                                        bins=100, range=(int(low), int(hi)), 
                                        label=labels['other'], color=colors['other'],
                                        histtype='step',)#alpha=0.5)
    # sqrt(n) error bars
    bin_errorbars(axs[0],n,bins,color=colors['sig'])
    bin_errorbars(axs[0],n2,bins2,color=colors['other'])
    
    # add in style features:
    axs[0].set_title(f'Cut and Count for {data_description}')
    axs[0].set_yscale('log')
    axs[0].set_xlabel('Reconstructed Momentum at Tracker Entrance [MeV/c]')
    axs[0].set_ylabel('Entries per bin')
    axs[0].grid(True)
    axs[0].legend()
    # second axis for cuts legend. placeholder for listing more cuts
    axs[1].set_axis_off()
    axs[1].text(0,1.05,'Cuts Applied to Signal Window')
    for i,s in enumerate(cuts_legend):
        offset=0.18*(i+1)
        axs[1].text(0,1.1-offset,s[0])
        axs[1].text(0,1.1-offset-0.06,s[1])
        
    plt.show()



