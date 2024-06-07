
import numpy as np
import pandas as pd

from plots import plottable

class MCTruth():

    def __init__(self, ):
        # process codes inferred from MCDataProducts/inc/ProcessCode.hh
        # currently just dealing with CE and DIO as first particle
        self.startcodes1 = { "CE" : 167,   # mu2eCeMinusEndpoint
                            "DIO" : 166,  # mu2eMuonDecayAtRest
                         }
        self.predlabels = ['Background','Signal']

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


