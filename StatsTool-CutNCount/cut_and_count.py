

import numpy as np
import argparse
import os.path
import awkward as ak

from recodata import ImportRecoData
import preprocess
from plots import PlotRecoMomEnt2


def cut_and_count(args):

    # load data
    filelist = os.path.join(args.folder,args.dataset)
    recodata = ImportRecoData(filelist, opt='testing')
    branches = recodata.Import_RecoFits(["demfit", "demlh", 'demmcsim','demtrkqual'])
    branches = preprocess.preprocessing1(branches)

    # apply cuts
    branches = recodata.cuts.apply_cuts_indicator(branches)
    cut_results = [branches[c+'_cut'] for c in recodata.cuts.cutsdict.keys()]

    # count events inside and outside signal window
    signal_count = np.prod(cut_results,axis=0).sum()
    nonsignal_count = len(branches) - signal_count
    print(f'Events in signal window: {signal_count}')
    print(f'Events outside signal window: {nonsignal_count}')

    # view results
    plots=['sig','other']
    labels = dict(zip(plots,['%i non-signal events' %nonsignal_count,'%i signal events' %signal_count]))
    cuts_legend = [['Momentum',f'p = {tuple(recodata.cuts.cutsdict["demfit_mom0"])} MeV/c',],
                   ['Time',f't0 = {tuple(recodata.cuts.cutsdict["demfit_t0"])} ns', ],
                    ['Maximum Radius',f'r = {tuple(recodata.cuts.cutsdict["demlh_maxr0"])} mm', ],
    ]
        #  ['Placeholder','cuts on additional parameters',]  ]
    PlotRecoMomEnt2(branches, args.mom_low,args.mom_high,labels,plots,cuts_legend,cut_results)

    # compare with mc truth info for particle type
    cut_results_f = ak.flatten(ak.prod(cut_results,axis=0),axis=None)
    cmat = recodata.mctruth.confusion_matrix(branches,cut_results_f)
    print('MC truth comparison:')
    recodata.mctruth.display_matrix(cmat,modes=['pd'])#,'plot'])#,'print'])
    

if __name__ == "__main__":

    #example: python cut_and_count.py --folder "/pnfs/mu2e/tape/phy-nts/nts/mu2e/ensemble-MixBB-CEDIO-1month-p95MeVc-Triggered/MDC2020ad_perfect_v1_2/tka/18/96" --dataset "nts.mu2e.ensemble-MixBB-CEDIO-1month-p95MeVc-Triggered.MDC2020ad_perfect_v1_2.0.tka" --treename "TrkAna" --branchname "trkana" --mom_low 95 --mom_hi 105
    parser = argparse.ArgumentParser(
        description='command arguments', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-d','--dataset', type=str, help='dataset',
        default="nts.mu2e.ensemble-MixBB-CEDIO-1month-p95MeVc-Triggered.MDC2020ad_perfect_v1_2.0.tka")
    parser.add_argument('-f','--folder', type=str, help='dataset location', default='.')
    parser.add_argument('-t','--treename', type=str, help='treename', default='TrkAna')
    parser.add_argument('-b','--branchname', type=str, help='branchname', default='trkana')
    parser.add_argument('-l','--mom_low', type=int, default=95, help='mom_low', )
    parser.add_argument('-g','--mom_high', type=int, default=115, help='mom_low', )
    args=parser.parse_args()
    
    cut_and_count(args)
    
    



