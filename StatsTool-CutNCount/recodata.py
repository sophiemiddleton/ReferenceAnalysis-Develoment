
import uproot

from cuts import Cuts
from mctruth import MCTruth

class ImportRecoData :

    def __init__(self, fileName, treeName="TrkAna", branchName="trkana", opt='su2020',use_crv=False):
        """ Initialise the Class Object """
        self.fileName = fileName
        self.treeName = treeName
        self.branchName = branchName
        self.cuts = Cuts(opt,use_crv)
        self.mctruth = MCTruth(self.cuts)

    def Import_RecoFits(self, leafs):
        """ import reconstructed trk ana"""
        # import with uproot
        #trkana = uproot.open(self.fileName+":"+str(self.treeName)+"/"+str(self.branchName))
        trkana = uproot.open({self.fileName : str(self.treeName)+"/"+str(self.branchName)})
        # find track fit branches for downstream (d) electron (em) loop helix (lh):
        # optional inclusion of other info such as MC truth (mcsim)
        filters = ["/"+str(leaf)+"/" for leaf in leafs]
        branches = trkana.arrays(filter_name=filters)
        return branches





