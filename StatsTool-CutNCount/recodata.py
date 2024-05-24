
import uproot

from cuts import Cuts



class ImportRecoData :

    def __init__(self, fileName, treeName="TrkAna", branchName="trkana", opt='su2020'):
        """ Initialise the Class Object """
        self.fileName = fileName
        self.treeName = treeName
        self.branchName = branchName
        self.cuts = Cuts(opt=opt)

    def Import_RecoFits(self, leafname, leafname_field):
        """ import reconstructed trk ana"""
        # import with uproot
        #trkana = uproot.open(self.fileName+":"+str(self.treeName)+"/"+str(self.branchName))
        trkana = uproot.open({self.fileName : str(self.treeName)+"/"+str(self.branchName)})
        # find track fit branches for downstream (d) electron (em) loop helix (lh):
        branches = trkana.arrays(filter_name=["/"+str(leafname)+"/", "/"+str(leafname_field)+"/"])
        return branches




