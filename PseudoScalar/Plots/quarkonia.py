import plots
import pandas as pd

df_Belle_Y1Stau = pd.read_csv('../data/quarkonia/Belle_Y1Stautau.csv')
df_BaBar_Y3Stau = pd.read_csv('../data/quarkonia/BaBar_Y3Stautau.csv')
df_BESIII_3gamma = pd.read_csv('../data/quarkonia/BESIII_3gamma.csv')
df_BESIII_gammainv = pd.read_csv('../data/quarkonia/BESIII_gammainv.csv')
df_BelleII_gammatau = pd.read_csv('../data/quarkonia/BelleII_4S_gammatau.csv')

Belle_Y1Stau = plots.PlotData(
    r'$\Upsilon(1S)\to\gamma a(\to\tau^+\tau^-)$' + '\n(Belle)',
    'tab:blue',
    (0.8, 3e3),
    True,
    df_Belle_Y1Stau['ma_GeV'],
    df_Belle_Y1Stau['gtau'],
    None
)

BaBar_Y3Stau = plots.PlotData(
    r'$\Upsilon(3S)\to\gamma \tau^+\tau^-$',
    'sienna',
    (1.8, 3e-1),
    True,
    df_BaBar_Y3Stau['ma_GeV'],
    df_BaBar_Y3Stau['gtau'],
    None
)

Belle_Y1Stau_proj = plots.PlotData(
    r'$\Upsilon(1S)\to\gamma a(\to\tau^+\tau^-)$' + '\n(Belle)',
    'tab:blue',
    (0.8, 3e3),
    False,
    df_Belle_Y1Stau['ma_GeV'],
    df_Belle_Y1Stau['gtau']/(5e4/24.91)**0.25,
    None
)

BESIII_3gamma = plots.PlotData(
    r'$J/\psi\to3\gamma$',
    'deeppink',
    (0.25, 0.1),
    True,
    df_BESIII_3gamma['ma_GeV'],
    df_BESIII_3gamma['gtau'],
    None
)

BESIII_gammainv = plots.PlotData(
    r'$J/\psi\to3\gamma$',
    'darkred',
    (0.15, 0.07),
    True,
    df_BESIII_gammainv['ma_GeV'],
    df_BESIII_gammainv['gtau'],
    df_BESIII_gammainv['gtau_7m']
)

BelleII_gammatau = plots.PlotData(
    r'$e^+e^-\to\gamma\tau^+\tau^-$',
    'sienna',
    (3.8, 3e-2),
    False,
    df_BelleII_gammatau['ma_GeV'],
    df_BelleII_gammatau['gtau'],
    None
)