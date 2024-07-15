import plots
import pandas as pd
from particle.literals import tau_minus
import numpy as np
from scipy.interpolate import CubicSpline

mtau = tau_minus.mass*1e-6 #TeV

df_gammainv = pd.read_csv('../data/direct_searches/gammainv.csv')
df_gammainv_proj = pd.read_csv('../data/direct_searches/gammainv_proj.csv')
df_ee3gamma = pd.read_csv('../data/direct_searches/ee3gamma.csv')
df_ee3gamma_proj = pd.read_csv('../data/direct_searches/ee3gamma_proj.csv')
df_eetaugamma = pd.read_csv('../data/direct_searches/eetaugamma.csv')
df_eetaugamma_proj = pd.read_csv('../data/direct_searches/eetaugamma_proj.csv')
df_ee3gamma = df_ee3gamma.sort_values(by='ma_GeV')
int_ee3gamma = CubicSpline(df_ee3gamma['ma_GeV'], df_ee3gamma['gtau'])
int_ee3gamma_proj = CubicSpline(df_ee3gamma_proj['ma_GeV'], df_ee3gamma_proj['gtau'])


gammainv = plots.PlotDataClosed(
    r'$e^+e^-\to \gamma +$ inv',
    'brown',
    (3e-3, 0.9e-1),
    True,
    df_gammainv['ma_GeV'],
    df_gammainv['gtau']
)

gammainv_proj = plots.PlotDataClosed(
    r'$e^+e^-\to \gamma +$ inv' + '\n' + r'  (50 ab$^{-1}$)',
    'brown',
    (3e-3, 5e-3),
    False,
    df_gammainv_proj['ma_GeV'],
    df_gammainv_proj['gtau']
)

ee3gamma = plots.PlotData(
    r'$e^+e^-\to 3\gamma$',
    'lightsalmon',
    (20e-2, 0.5),
    True,
    np.logspace(np.log10(min(df_ee3gamma['ma_GeV'])), np.log10(2*mtau)+3, 200),
    [int_ee3gamma(ma) for ma in np.logspace(np.log10(min(df_ee3gamma['ma_GeV'])), np.log10(2*mtau)+3, 200)],
    None
)

ee3gamma_proj = plots.PlotData(
    r'$e^+e^-\to 3\gamma$' +'\n' + r'(50 ab$^{-1}$)',
    'lightsalmon',
    (20e-2, 2.5e-2),
    False,
    np.logspace(np.log10(min(df_ee3gamma_proj['ma_GeV'])), np.log10(2*mtau)+3, 200),
    [int_ee3gamma_proj(ma) for ma in np.logspace(np.log10(min(df_ee3gamma_proj['ma_GeV'])), np.log10(2*mtau)+3, 200)],
    None
)

eetaugamma = plots.PlotData(
    r'$e^+e^-\to \tau^+\tau^-\gamma\gamma$',
    'red',
    (1, 1.7e-2),
    True,
    df_eetaugamma['ma_GeV'],
    df_eetaugamma['cl']*mtau,
    None
)

eetaugamma_proj = plots.PlotData(
    r'$e^+e^-\to \tau^+\tau^-\gamma\gamma$' + '\n' + r'(50 ab$^{-1}$)',
    'red',
    (1, 1e-3),
    False,
    df_eetaugamma_proj['ma_GeV'],
    df_eetaugamma_proj['cl']*mtau,
    None
)
