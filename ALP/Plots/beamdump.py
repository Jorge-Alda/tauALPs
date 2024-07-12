import plots
import pandas as pd
import particle.literals
import numpy as np

me = particle.literals.e_minus.mass/1000

e137sup = pd.read_csv('../data/beam_dump/E137_sup.csv')
konsup = pd.read_csv('../data/beam_dump/Konaka_sup.csv')
riosup = pd.read_csv('../data/beam_dump/Riordan_sup.csv')
rioinf = pd.read_csv('../data/beam_dump/Riordan_inf.csv')
photons = pd.read_csv('../data/beam_dump/photons.csv')
photons_tau = pd.read_csv('../data/beam_dump/photons_tau.csv')

e137 = plots.PlotData(
    'Beam dump',
    'chocolate',
    (2e-3, 1),
    True,
    e137sup['ma_GeV'],
    e137sup['gee']/me*1000,
    [5e-3/0.246 for i in e137sup.index]
)

konaka = plots.PlotData(
    '',
    'chocolate',
    (2e-3, 1),
    True,
    konsup['ma_GeV'],
    konsup['gee']/me*1000,
    [2e-7*np.pi**0.5/me*1000 for i in konsup.index]
)

riordan = plots.PlotData(
    '',
    'chocolate',
    (2e-3, 1),
    True,
    riosup['ma_GeV'],
    riosup['gee']/me*1000,
    rioinf['gee']/me*1000
)

beamdump_combined = plots.PlotData(
    'Beam dump\n' + r'$e^+e^-$',
    'chocolate',
    (1.3e-3, 1),
    True,
    riosup['ma_GeV'],
    riosup['gee']/me*1000,
    [5e-3/0.246 for i in riosup.index if riosup['ma_GeV'][i] <= max(e137sup['ma_GeV']) ] + [2e-7*np.pi**0.5/me*1000 for i in riosup.index if riosup['ma_GeV'][i] > max(e137sup['ma_GeV']) and riosup['ma_GeV'][i] <= max(konsup['ma_GeV']) ] + [rioinf['gee'][i]/me*1000 for i in riosup.index if riosup['ma_GeV'][i] > max(konsup['ma_GeV'])]
)

beamdump_photons = plots.PlotData(
    'Beam dump\n' + r'          $\gamma\gamma$',
    'chocolate',
    (7e-3, 650),
    True,
    photons['ma_GeV'],
    photons['cl_inf'],
    photons['cl_sup']
)

beamdump_photons_tau = plots.PlotData(
    'Beam dump',
    'chocolate',
    (1.2e-2, 650),
    True,
    photons_tau['ma_GeV'],
    photons_tau['ctau_inf'],
    photons_tau['ctau_sup']
)