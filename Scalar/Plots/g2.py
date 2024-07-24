import plots
import pandas as pd

df_g2_tau = pd.read_csv('../data/anomalous_moments/g2tau.csv')

BelleII_g2tau = plots.PlotData(
    r'$(g-2)_\tau$ (Belle II)',
    'purple',
    (1.2e-3,7e-3),
    False,
    df_g2_tau['ma_GeV'],
    df_g2_tau['c_g2tau_BelleII'],
    None
)

ATLAS_g2tau = plots.PlotData(
    r'$(g-2)_\tau$ (ATLAS, ' + r'$q\bar{q}\to \tau^+\tau^-$)',
    'purple',
    (1.2e-1, 0.25),
    True,
    df_g2_tau['ma_GeV'],
    df_g2_tau['c_g2tau_ATLAS'],
    None
)

CMS_g2tau = plots.PlotData(
    r'$(g-2)_\tau$ (ATLAS, ' + r'$q\bar{q}\to \tau^+\tau^-$)',
    'purple',
    (1.2e-3, 0.25),
    True,
    df_g2_tau['ma_GeV'],
    df_g2_tau['c_g2tau_CMS24'],
    None
)