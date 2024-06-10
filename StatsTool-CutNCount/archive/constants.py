# Author : S Middleton
# Date : 2021
# Purpose : Stores any constants used by the analysis

class Constants:

        def __init__(self):

            self.livegate = 700 #TODO- should be optimized
            self.POT= 3.6e20 #TODO - needs to come from database
            self.muonstopsperPOT = 1.55e-3 #TODO - datavased
            self.sim_ce_eff = 1
            self.sim_dio_eff = 1
            self.capturesperStop = 0.61
            self.decaysperStop = 0.39
            self.fixed_window_lower = 103.85 #TODO should be optimized
            self.fixed_window_upper = 105.1


            print("===================Information:============================")
            print("Number of Protons on Target:", self.POT)
            print("Target Material:", target)
            print("Muon Stopping Rate:", self.muonstopsperPOT)
            print("Captures Per Stop:", self.capturesperStop)
            print("Decays Per Stop:", self.decaysperStop)
            print("Default Signal Window (mom):", self.fixed_window_lower,"to",self.fixed_window_upper)
            print("===========================================================")
