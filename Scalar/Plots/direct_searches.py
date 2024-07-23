import plots
import pandas as pd
from particle.literals import tau_minus
import numpy as np
from scipy.interpolate import CubicSpline

mtau = tau_minus.mass*1e-6 #TeV

df_gammainv = pd.read_csv('../data/direct_searches/gammainv.csv')
df_ee3gamma = pd.read_csv('../data/direct_searches/ee3gamma.csv')
df_eetaugamma = pd.read_csv('../data/direct_searches/tautaugammagamma.csv')

gammainv_BaBar = plots.PlotData(
    r'$e^+e^-\to \gamma +$ inv',
    'brown',
    (0.5e-1, 0.7),
    True,
    df_gammainv.loc[df_gammainv['ma_GeV']<0.7]['ma_GeV'],
    df_gammainv.loc[df_gammainv['ma_GeV']<0.7]['gtau_BaBar'],
    df_gammainv.loc[df_gammainv['ma_GeV']<0.7]['gtau_3m']
)

gammainv = plots.PlotData(
    r'$e^+e^-\to \gamma +$ inv',
    'brown',
    (0.5e-1, 0.7),
    True,
    df_gammainv.loc[df_gammainv['ma_GeV']<1.25]['ma_GeV'],
    df_gammainv.loc[df_gammainv['ma_GeV']<1.25]['gtau_20fb-1'],
    df_gammainv.loc[df_gammainv['ma_GeV']<1.25]['gtau_3m']
)

gammainv_proj = plots.PlotData(
    r'$e^+e^-\to \gamma +$ inv  (50 ab$^{-1}$)',
    'brown',
    (1.1e-3, 2.8e-2),
    False,
    df_gammainv['ma_GeV'],
    df_gammainv['gtau_50ab-1'],
    df_gammainv['gtau_3m']
)

ee3gamma_445pb = plots.PlotData(
    r'$e^+e^-\to 3\gamma$',
    'red',
    (1.2, 1.9),
    True,
    df_ee3gamma['ma_GeV'],
    df_ee3gamma['gtau_445pb-1'],
    None
)

ee3gamma = plots.PlotData(
    r'$e^+e^-\to 3\gamma$',
    'red',
    (1, 5),
    True,
    df_ee3gamma['ma_GeV'],
    df_ee3gamma['gtau_20fb-1'],
    None
)

ee3gamma_proj = plots.PlotData(
    r'$e^+e^-\to 3\gamma$' +'\n' + r'(50 ab$^{-1}$)',
    'red',
    (1.55, 0.83e-1),
    False,
    df_ee3gamma['ma_GeV'],
    df_ee3gamma['gtau_50ab-1'],
    None,
    rotation=-35
)

eetaugamma = plots.PlotData(
    r'$e^+e^-\to \tau^+\tau^-\gamma\gamma$',
    'xkcd:pumpkin orange',
    (0.83, 1e-2),
    True,
    df_eetaugamma['ma_GeV'],
    df_eetaugamma['gtau_20fb-1'],
    None,
    rotation=-35
)

eetaugamma_proj = plots.PlotData(
    r'$e^+e^-\to \tau^+\tau^-\gamma\gamma$',
    'xkcd:pumpkin orange',
    (1.3, 2.6e-2),
    False,
    df_eetaugamma['ma_GeV'],
    df_eetaugamma['gtau_50ab-1'],
    None,
    rotation=-35
)
