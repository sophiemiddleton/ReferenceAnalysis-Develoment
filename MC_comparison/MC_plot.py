# Monte Carlo plots
# Make plots showing Monte Carlo truth

# Author: Leo Borrel
# Date: 2024-05-14

import numpy as np
import uproot
import awkward as ak
import matplotlib.pyplot as plt


# import ROOT data
input_file = uproot.open("nts.mu2e.ensemble-1BB-CEDIOCRYCosmic-600000s-p95MeVc-Triggered.MDC2020ad_perfect_v1_3.0.tka")
input_tree = input_file['TrkAna']['trkana']
array = input_tree.arrays(library='ak')
#print(array.type.show()) # show the name of all the branches

# create momentum branch
array['mom'] = np.sqrt((array['demfit','mom','fCoordinates','fX'])**2 + (array['demfit','mom','fCoordinates','fY'])**2 + (array['demfit','mom','fCoordinates','fZ'])**2)

# select gen code and proc code MC information and flatten the array (for counting purpose)
gen_array = ak.flatten(array['demmcsim','gen'][...,:1], axis=None)
proc_array = ak.flatten(array['demmcsim','startCode'][...,:1], axis=None)

# MC gen code can be found in Offline/MCDataProducts/inc/genId.hh
gen_code = ['unknown', 'particleGun', 'CeEndpoint',
            'cosmicToy', 'cosmicDYB', 'cosmic', 'obsolete1', #6
            'dioTail', 'obsolete2', 'obsolete3', 'obsolete4', 'ExternalRPC', #11
            'muonCapture', 'muonDecayInFlight', 'ejectedProtonGun', #14
            'piEplusNuGun', 'primaryProtonGun', 'fromG4BLFile', 'ePlusfromStoppedPi', #18
            'ejectedNeutronGun', 'ejectedPhotonGun', 'nuclearCaptureGun', 'InternalRPC', #22
            'extMonFNALGun', 'fromStepPointMCs', 'stoppedMuonGun', 'PiCaptureCombined', #26
            'MARS', 'StoppedParticleReactionGun', 'bremElectronGun', 'muonicXRayGun', #30
            'fromSimParticleStartPoint', 'fromSimParticleCompact', 'StoppedParticleG4Gun', #33
            'CaloCalib', 'InFlightParticleSampler', 'muplusDecayGun', 'StoppedMuonXRayGammaRayGun', #37
            'cosmicCRY', 'pbarFlat', 'fromAscii', 'ExternalRMC', 'InternalRMC', 'CeLeadingLog', 'cosmicCORSIKA', #44
            'MuCapProtonGenTool', 'MuCapDeuteronGenTool', 'DIOGenTool', 'MuCapNeutronGenTool', #48
            'MuCapPhotonGenTool', 'MuCapGammaRayGenTool', 'CeLeadingLogGenTool', 'MuplusMichelGenTool', #52
            'gammaPairProduction', #53
            'lastEnum' #54
            ]

# MC process code can be found in Offline/MCDataProducts/inc/ProcessCode
proc_code = [
      'unknown',                'AlphaInelastic',          'annihil',             'AntiLambdaInelastic', # 3
      'AntiNeutronInelastic',   'AntiOmegaMinusInelastic', 'AntiProtonInelastic', 'AntiSigmaMinusInelastic', # 7
      'AntiSigmaPlusInelastic', 'AntiXiMinusInelastic',    'AntiXiZeroInelastic', 'CHIPSNuclearCaptureAtRest', # 11
      'compt',                  'conv',                    'Decay',               'DeuteronInelastic', # 15
      'eBrem',                  'eIoni',                   'ElectroNuclear',      'hBrems', # 19
      'hElastic',               'hIoni',                   'hPairProd',           'ionIoni',  # 23
      'KaonMinusInelastic',     'KaonPlusInelastic',       'KaonZeroLInelastic',  'KaonZeroSInelastic', # 27
      'LambdaInelastic',        'msc',                     'muBrems',             'muIoni',  # 31
      'muMinusCaptureAtRest',   'muMsc',                   'muPairProd',          'nCapture',  # 35
      'NeutronInelastic',       'nFission',                'nKiller',             'OmegaMinusInelastic', # 39
      'phot',                   'PhotonInelastic',         'PionMinusInelastic',  'PionPlusInelastic', # 43
      'PositronNuclear',        'ProtonInelastic',         'SigmaMinusInelastic', 'SigmaPlusInelastic', # 47
      'StepLimiter',            'Transportation',          'TritonInelastic',     'XiMinusInelastic', # 51
      'XiZeroInelastic',        'mu2eLowEKine',            'mu2eKillerVolume',    'mu2eMaxSteps',  # 55
      'mu2ePrimary',            'mu2eSpecialCutsProcess',  'hadElastic',          'CoulombScat', # 59
      'nuclearStopping',        'mu2eMaxGlobalTime',       'TNuclearCapture',     'muMinusAtomicCapture', # 63
      'MuAtomDecay',            'Rayl',                    'ionInelastic',        'He3Inelastic', # 67
      'alphaInelastic',         'AntiHe3InelasticProcess', 'AntiAlphaInelasticProcess', 'AntiDeuteronInelastic', # 71
      'dInelastic',             'tInelastic',              'RadioactiveDecay',    'CHIPS_Inelastic', # 75
      'NotSpecified',           'hFritiofCaptureAtRest',   'hBertiniCaptureAtRest', 'AntiTritonInelasticProcess', # 79
      'anti_He3Inelastic',      'anti_alphaInelastic',     'anti_deuteronInelastic', 'anti_lambdaInelastic', # 83
      'anti_neutronInelastic',  'anti_omega_MinusInelastic', 'anti_protonInelastic', 'anti_sigma_PlusInelastic',  # 87
      'anti_sigma_MinusInelastic', 'anti_tritonInelastic', 'anti_xi_MinusInelastic', 'anti_xi0Inelastic',  # 91
      'kaon_PlusInelastic',     'kaon_MinusInelastic',     'kaon0LInelastic',     'kaon0SInelastic', # 95
      'lambdaInelastic',        'neutronInelastic',        'omega_MinusInelastic', 'pi_PlusInelastic',  # 99
      'pi_MinusInelastic',      'protonInelastic',         'sigma_PlusInelastic', 'sigma_MinusInelastic', # 103
      'sigma0Inelastic',        'xi_MinusInelastic',       'xi0Inelastic',        'positronNuclear', # 107
      'electronNuclear',        'photonNuclear',           'antilambdaInelastic', 'DecayWithSpin', # 111
      'ionElastic',             'EMCascade',               'DIO',                 'NuclearCapture', # 115
      'muonNuclear',            'GammaToMuPair',           'AnnihiToMuPair',      'ee2hadr', # 119
      'G4MinEkineCuts',         'G4MaxTimeCuts',           'OpAbsorption',        'OpBoundary', # 123
      'Scintillation',          'inelastic',               'G4ErrorEnergyLoss',   'G4ErrorStepLengthLimit', # 127
      'G4ErrorMagFieldLimit',   'ePairProd',               'mu2eFieldPropagator', 'mu2eRecorderProcess',  # 131
      'mu2eProtonInelastic',    'RadioactiveDecayBase',    'B_PlusInelastic',     'B_MinusInelastic', # 135
      'B0Inelastic',            'Bc_PlusInelastic',        'Bc_MinusInelastic',   'Bs0Inelastic', # 139
      'D_PlusInelastic',        'D_MinusInelastic',        'D0Inelastic',         'Ds_PlusInelastic', # 143
      'Ds_MinusInelastic',      'anti_B0Inelastic',        'anti_Bs0Inelastic',   'anti_D0Inelastic', # 147
      'anti_lambda_bInelastic', 'anti_lambda_c_PlusInelastic', 'anti_omega_b_MinusInelastic', 'anti_omega_c0Inelastic', # 151
      'anti_xi_b_MinusInelastic', 'anti_xi_b0Inelastic',   'anti_xi_c_PlusInelastic', 'anti_xi_c0Inelastic', # 155
      'lambda_bInelastic',      'lambda_c_PlusInelastic',  'omega_b_MinusInelastic', 'omega_c0Inelastic', # 159
      'xi_b_MinusInelastic',    'xi_b0Inelastic',          'xi_c_PlusInelastic',  'xi_c0Inelastic', # 163
      # stopped-muon physics processes, specific to Mu2e
      'truncated',       'mu2eMuonCaptureAtRest',  'mu2eMuonDecayAtRest',       'mu2eCeMinusEndpoint', # 167
      'mu2eCeMinusLeadingLog',   'mu2eCePlusEndpoint',  'mu2eDIOLeadingLog', 'mu2eInternalRMC',  # 171
      'mu2eExternalRMC',         'mu2eFlateMinus',      'mu2eFlatePlus', 'mu2eFlatPhoton', # 175
      'mu2eCePlusLeadingLog', 'mu2ePionCaptureAtRest', 'mu2eExternalRPC', 'mu2eInternalRPC', # 179
      'mu2eCaloCalib', 'mu2ePienu', 'mu2eunused7', 'mu2eunused8', # 183
      'uninitialized', 'NoProcess', 'GammaGeneralProc', # 186
      'mu2eGammaConversion', 'Radioactivation', 'nCaptureHP', 'nFissionHP', # 190
      'lastEnum'
      ]

# Count the number of particle with each gen code and process code
gen_count = []
print('process code counts:')
for gen_idx, gen_name in enumerate(gen_code):
    N_gen = ak.num(gen_array[gen_array == gen_idx], axis=0)
    if N_gen != 0:
        gen_count.append((gen_idx, gen_name, N_gen.item()))

print(gen_count)

proc_count = []
print('process code counts:')
for proc_idx, proc_name in enumerate(proc_code):
    N_proc = ak.num(proc_array[proc_array == proc_idx], axis=0)
    if N_proc != 0:
        proc_count.append((proc_idx, proc_name, N_proc.item()))

print(proc_count)

gen_array = array['demmcsim','gen'][...,:1]
cut = ak.any(gen_array == 38, axis=1)
mask = ak.mask(array, cut)

# Plot

mom_plot = []
time_plot = []
name_plot = []
for (index_proc, name_proc, N_proc) in proc_count:
    array_proc = array['demmcsim','startCode'][..., :1]
    cut_proc = ak.any(array_proc == index_proc, axis=1)
    mask = ak.mask(array, cut_proc)
    flat_mom = ak.flatten(mask['mom'][...,:1], axis=None)
    mom_plot.append(ak.to_numpy(flat_mom))
    flat_time = ak.flatten(mask['demfit','time'][...,:1], axis=None)
    time_plot.append(ak.to_numpy(flat_time))
    name_plot.append(name_proc)

array_np = ak.to_numpy(ak.flatten(array['mom'][...,:1], axis=None))

n_bins = 200
plot_range = (0, 200)
array_hist, array_binedge = np.histogram(array_np, bins=n_bins, range=plot_range)
array_bincenter = 0.5 * (array_binedge[1:] + array_binedge[:-1])

fig,ax = plt.subplots(1,1)
ax.hist(mom_plot, bins=n_bins, range=plot_range, histtype='stepfilled', stacked=True, label=name_plot)

ax.set_xlabel('mom')
ax.set_ylabel('# of events')
ax.legend()

fig,ax = plt.subplots(1,1)
ax.hist(time_plot, bins=n_bins, range=(0, 1700), histtype='stepfilled', stacked=True, label=name_plot)

ax.set_xlabel('time')
ax.set_ylabel('# of events')
ax.legend()


fig,ax = plt.subplots(1,1)
ax.hist(mom_plot[-2], bins=100, range=(95, 105), histtype='stepfilled', label=name_plot[-2])

ax.set_yscale('log')
ax.set_xlabel('mom')
ax.set_ylabel('# of events')
ax.legend()

plt.show()
