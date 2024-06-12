
import numpy as np
import pandas as pd

from plots import plottable

class MCTruth():

    def __init__(self, cuts):
        # process codes inferred from MCDataProducts/inc/ProcessCode.hh
        # currently just dealing with CE and DIO as first particle
        self.startcodes1 = { "CE" : 167,   # mu2eCeMinusEndpoint
                            "DIO" : 166,  # mu2eMuonDecayAtRest
                         }
        self.predlabels = ['Background','Signal']
        self.cuts = cuts

    def confusion_matrix(self,data,cut_results,plot=True,printout=True,pdview=False):
        """ confusion matrix between true particle (rows) and background/signal prediction (columns)"""
        cmat = np.zeros((len(self.startcodes1),2),dtype=int)
        for i,si in enumerate(self.startcodes1.values()):  # true particle type
            for j in [0,1]:  # background,signal
                cmat[i,j] = np.sum((cut_results==j) & (data['mcproc1']==si))
                #print(s,j,cmat[i,j-1])
        return cmat

    def display_matrix(self,mat,modes=['pd']):
        # several options to view (basic, plot, pd)
        if 'print' in modes: # (if not using pandas)
            print('\t','\t'.join(self.predlabels))
            [print(list(self.startcodes1.keys())[i],'\t',
               '\t\t'.join(list(mat[i].astype(str)))) for i in range(mat.shape[0])]
        if 'plot' in modes:
            plottable(mat,list(self.startcodes1.keys()),self.predlabels)
        if 'pd' in modes:
            mat_df = pd.DataFrame(mat,index=list(self.startcodes1.keys()),columns=self.predlabels)
            print(mat_df)

    def cut_survival(self,data,cut_results,other=True):
        """ for each MC truth particle type or category (columns), determine whether track passes 
        each cut with cuts applied sequentially (rows)"""
        # whether track survives each sequential cut
        survival = np.cumprod(np.array(cut_results),axis=0)
        # MC truth first process for each surviving track
        survival=np.array(data['mcproc1']) * survival
        survival = survival[:,np.unique(np.nonzero(survival)[1])]

        # look at some specific process types and leave rest in other category
        survival_table = pd.DataFrame(index=self.cuts.cutsdict.keys())
        if other: otherproc1 = np.unique(data['mcproc1'])
        for particletype in self.startcodes1.keys():
            survival_table[particletype] = np.count_nonzero(survival==self.startcodes1[particletype],axis=1)
            if other: otherproc1 = otherproc1[otherproc1!=self.startcodes1[particletype]]
        # other processes from cosmic rays currently combined into one category
        if other: survival_table['Other'] = np.count_nonzero((survival!=0) & 
                                                   (np.sum([survival==p for p in otherproc1],axis=0)),axis=1)        
        return survival_table
