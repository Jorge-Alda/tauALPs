import plots
import pandas as pd
from particle.literals import tau_minus

mtau = tau_minus.mass*1e-6


df_gammainv = pd.read_csv('../data/direct_searches/gammainv.csv')
df_gammainv_proj = pd.read_csv('../data/direct_searches/gammainv_proj.csv')
df_ee3gamma = pd.read_csv('../data/direct_searches/ee3gamma.csv')
df_ee3gamma_proj = pd.read_csv('../data/direct_searches/ee3gamma_proj.csv')
df_eetaugamma = pd.read_csv('../data/direct_searches/eetaugamma.csv')
df_eetaugamma_proj = pd.read_csv('../data/direct_searches/eetaugamma_proj.csv')


gammainv = plots.PlotDataClosed(
    r'$e^+e^-\to \gamma +$ inv',
    'brown',
    (3e-3, 4e-2),
    True,
    df_gammainv['ma_GeV'],
    df_gammainv['gtau']
)

gammainv_proj = plots.PlotDataClosed(
    r'$e^+e^-\to \gamma +$ inv' + '\n' + r'  (50 ab$^{-1}$)',
    'brown',
    (3e-3, 2e-3),
    False,
    df_gammainv_proj['ma_GeV'],
    df_gammainv_proj['gtau']
)

ee3gamma = plots.PlotData(
    r'$e^+e^-\to 3\gamma$',
    'lightsalmon',
    (0.2, 0.17),
    True,
    df_ee3gamma['ma_GeV'],
    df_ee3gamma['gtau'],
    None
)

ee3gamma_proj = plots.PlotData(
    r'$e^+e^-\to 3\gamma$' +'\n' + r'(50 ab$^{-1}$)',
    'lightsalmon',
    (16e-2, 1.4e-2),
    False,
    df_ee3gamma_proj['ma_GeV'],
    df_ee3gamma_proj['gtau'],
    None
)

eetaugamma = plots.PlotData(
    r'$e^+e^-\to \tau^+\tau^-\gamma\gamma$',
    'red',
    (1, 120*mtau),
    True,
    df_eetaugamma['ma_GeV'],
    df_eetaugamma['cl']*mtau,
    None
)

eetaugamma_proj = plots.PlotData(
    r'$e^+e^-\to \tau^+\tau^-\gamma\gamma$' + '\n' + r'(50 ab$^{-1}$)',
    'red',
    (1, 0.75*mtau),
    False,
    df_eetaugamma_proj['ma_GeV'],
    df_eetaugamma_proj['cl']*mtau,
    None
)
