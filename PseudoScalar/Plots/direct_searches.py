import plots
import pandas as pd
from particle.literals import tau_minus
import numpy as np
from scipy.interpolate import CubicSpline

mtau = tau_minus.mass*1e-6


df_gammainv = pd.read_csv('../data/direct_searches/gammainv.csv')
df_ee3gamma = pd.read_csv('../data/direct_searches/ee3gamma.csv')
df_eetaugamma = pd.read_csv('../data/direct_searches/tautaugammagamma.csv')

gammainv_BaBar = plots.PlotData(
    r'$e^+e^-\to \gamma +$ inv',
    'brown',
    (1.3e-2, 8e-2),
    True,
    df_gammainv.loc[df_gammainv['ma_GeV']<0.75]['ma_GeV'],
    df_gammainv.loc[df_gammainv['ma_GeV']<0.75]['gtau_BaBar'],
    df_gammainv.loc[df_gammainv['ma_GeV']<0.75]['gtau_3m']
)

gammainv = plots.PlotData(
    r'$e^+e^-\to \gamma +$ inv',
    'brown',
    (3e-3, 4e-2),
    True,
    df_gammainv.loc[df_gammainv['ma_GeV']<1.2]['ma_GeV'],
    df_gammainv.loc[df_gammainv['ma_GeV']<1.2]['gtau_20fb-1'],
    df_gammainv.loc[df_gammainv['ma_GeV']<1.2]['gtau_3m']
)

gammainv_proj = plots.PlotData(
    r'$e^+e^-\to \gamma +$ inv' + '\n' + r'  (50 ab$^{-1}$)',
    'brown',
    (3e-3, 2e-3),
    False,
    df_gammainv['ma_GeV'],
    df_gammainv['gtau_50ab-1'],
    df_gammainv['gtau_3m']
)

ee3gamma_445pb = plots.PlotData(
    r'$e^+e^-\to 3\gamma$',
    'red',
    (1.3, 4),
    True,
    df_ee3gamma['ma_GeV'],
    df_ee3gamma['gtau_445pb-1'],
    None
)

ee3gamma = plots.PlotData(
    r'$e^+e^-\to 3\gamma$',
    'red',
    (1.3, 2.5),
    True,
    df_ee3gamma['ma_GeV'],
    df_ee3gamma['gtau_20fb-1'],
    None
)

ee3gamma_proj = plots.PlotData(
    r'$e^+e^-\to 3\gamma$' +'\n' + r'(50 ab$^{-1}$)',
    'red',
    (2.8, 0.08),
    False,
    df_ee3gamma['ma_GeV'],
    df_ee3gamma['gtau_50ab-1'],
    None
)

eetaugamma = plots.PlotData(
    r'$e^+e^-\to \tau^+\tau^-\gamma\gamma$',
    'lightsalmon',
    (0.8, 1e-2),
    True,
    df_eetaugamma['ma_GeV'],
    df_eetaugamma['gtau_20fb-1'],
    None,
    rotation=-30
)

eetaugamma_proj = plots.PlotData(
    r'$e^+e^-\to \tau^+\tau^-\gamma\gamma$',
    'lightsalmon',
    (0.8, 1e-2),
    False,
    df_eetaugamma['ma_GeV'],
    df_eetaugamma['gtau_50ab-1'],
    None,
    rotation = -30
)
