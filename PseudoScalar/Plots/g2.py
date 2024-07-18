import plots
import pandas as pd

df_g2e = pd.read_csv('../data/anomalous_moments/g2e.csv')
df_g2mu = pd.read_csv('../data/anomalous_moments/g2mu.csv')
df_g2tau = pd.read_csv('../data/anomalous_moments/g2tau.csv')

BelleII_g2tau = plots.PlotData(
    r'$(g-2)_\tau$ (Belle II)',
    'purple',
    (1e-1, 2e-2),
    False,
    df_g2tau['ma_GeV'],
    df_g2tau['c_g2tau_BelleII'],
    None
)

ATLAS_g2tau = plots.PlotData(
    r'$(g-2)_\tau$' + '\n(ATLAS, ' + r'$q\bar{q}\to \tau^+\tau^-$)',
    'purple',
    (1.5e-3, 0.25),
    True,
    df_g2tau['ma_GeV'],
    df_g2tau['c_g2tau_ATLAS'],
    None
)
