import plots
import pandas as pd

df_Belle_Y1Stau = pd.read_csv('../data/quarkonia/Belle_Y1Stautau.csv')
df_BaBar_Y1Stau = pd.read_csv('../data/quarkonia/BaBar_Y1Stautau.csv')
df_BaBar_Y3Stau = pd.read_csv('../data/quarkonia/BaBar_Y3Stautau.csv')
df_Belle_Y1Smu = pd.read_csv('../data/quarkonia/Belle_Y1Smumu.csv')
df_BaBar_Y1Smu = pd.read_csv('../data/quarkonia/BaBar_Y1Smumu.csv')
df_BaBar_Y2Smu = pd.read_csv('../data/quarkonia/BaBar_Y2Smumu.csv')
df_BaBar_Y3Smu = pd.read_csv('../data/quarkonia/BaBar_Y3Smumu.csv')
df_BaBar_Y3Stot = pd.read_csv('../data/quarkonia/BaBar_Y3S_tot.csv')
df_BESIII_Jpsimu = pd.read_csv('../data/quarkonia/BESIII_Jpsimumu.csv')
df_BelleII_Y4S3g_lfu = pd.read_csv('../data/quarkonia/BelleII_Y4S3g_lfu.csv')
df_BESIII_Jpsi3g_lfu = pd.read_csv('../data/quarkonia/BESIII_Jpsi3g_lfu.csv')
df_BelleII_Y4S3g_tau = pd.read_csv('../data/quarkonia/BelleII_Y4S3g_tau.csv')
df_BESIII_Jpsi3g_tau = pd.read_csv('../data/quarkonia/BESIII_Jpsi3g_tau.csv')


Belle_Y1Stau = plots.PlotData(
    r'$\Upsilon(1S)\to\gamma a(\to\tau^+\tau^-)$' + '\n(Belle)',
    'tab:blue',
    (0.8, 3e3),
    True,
    df_Belle_Y1Stau['ma_GeV'],
    df_Belle_Y1Stau['cl'],
    None
)

BaBar_Y1Stau = plots.PlotData(
    r'$\Upsilon(1S)\to\gamma a(\to\tau^+\tau^-)$' + '\n(BaBar)',
    'tab:orange',
    (0.8, 3e4),
    True,
    df_BaBar_Y1Stau['ma_GeV'],
    df_BaBar_Y1Stau['cl'],
    None
)

BaBar_Y1Smu = plots.PlotData(
    r'$\Upsilon(1S)\to\gamma a(\to\mu^+\mu^-)$' + '\n(BaBar)',
    'tab:orange',
    (0.8, 3e4),
    True,
    df_BaBar_Y1Stau['ma_GeV'],
    df_BaBar_Y1Stau['cl'],
    None
)

BaBar_Y3Stau = plots.PlotData(
    r'$\Upsilon(3S)\to\gamma a(\to\tau^+\tau^-)$' + '\n(BaBar)',
    'tab:green',
    (1.2, 100),
    True,
    df_BaBar_Y3Stau['ma_GeV'],
    df_BaBar_Y3Stau['cl'],
    None
)

Belle_Y1Smu = plots.PlotData(
    r'$\Upsilon(1S)\to\gamma a(\to\mu^+\mu^-)$' + '\n(Belle)',
    'tab:purple',
    (0.1, 1e3),
    True,
    df_Belle_Y1Smu['ma_GeV'],
    df_Belle_Y1Smu['cl'],
    None
)

BaBar_Y1Smu = plots.PlotData(
    r'$\Upsilon(1S)\to\gamma a(\to\mu^+\mu^-)$' + '\n(BaBar)',
    'tab:grey',
    (0.1, 1e3),
    True,
    df_BaBar_Y1Smu['ma_GeV'],
    df_BaBar_Y1Smu['cl'],
    None
)

BaBar_Y2Smu = plots.PlotData(
    r'$\Upsilon(2S)\to\gamma a(\to\mu^+\mu^-)$' + '\n(BaBar)',
    'tab:pink',
    (0.1, 1e3),
    True,
    df_BaBar_Y2Smu['ma_GeV'],
    df_BaBar_Y2Smu['cl'],
    None
)

BaBar_Y3Smu = plots.PlotData(
    r'$\Upsilon(3S)\to\gamma a(\to\mu^+\mu^-)$' + '\n(BaBar)',
    'tab:red',
    (0.1, 1e3),
    True,
    df_BaBar_Y3Smu['ma_GeV'],
    df_BaBar_Y3Smu['cl'],
    None
)

BaBar_Y3Stot = plots.PlotData(
    r'$\Upsilon(3S)\to\gamma a$' + '\n(BaBar)',
    'tab:green',
    (0.8, 100),
    True,
    df_BaBar_Y3Stot['ma_GeV'],
    df_BaBar_Y3Stot['cl'],
    None
)

BESIII_Jpsimu = plots.PlotData(
    r'$J/\psi\to\gamma a(\to\mu^+\mu^-)$' + '\n(BESIII)',
    'tab:brown',
    (0.1, 1e3),
    True,
    df_BESIII_Jpsimu['ma_GeV'],
    df_BESIII_Jpsimu['cl'],
    None
)

BESIII_Jpsi3g_lfu = plots.PlotData(
    r'$J/\psi\to\gamma a(\to\gamma\gamma)$' + '\n(BESIII)',
    'tab:olive',
    (0.1, 1e3),
    True,
    df_BESIII_Jpsi3g_lfu['ma_GeV'],
    df_BESIII_Jpsi3g_lfu['cl'],
    None
)

BelleII_Y4S3g_lfu = plots.PlotData(
    r'$\Upsilon(4S)\to\gamma a(\to\gamma\gamma)$' + '\n(Belle II)',
    'tab:cyan',
    (0.1, 1e3),
    True,
    df_BelleII_Y4S3g_lfu['ma_GeV'],
    df_BelleII_Y4S3g_lfu['cl'],
    None
)

BESIII_Jpsi3g_tau = plots.PlotData(
    r'$J/\psi\to\gamma a(\to\gamma\gamma)$' + '\n(BESIII)',
    'tab:red',
    (0.1, 1e3),
    True,
    df_BESIII_Jpsi3g_tau['ma_GeV'],
    df_BESIII_Jpsi3g_tau['cl'],
    None
)

BelleII_Y4S3g_tau = plots.PlotData(
    r'$\Upsilon(4S)\to\gamma a(\to\gamma\gamma)$' + '\n(Belle II)',
    'tab:purple',
    (0.1, 1e3),
    True,
    df_BelleII_Y4S3g_tau['ma_GeV'],
    df_BelleII_Y4S3g_tau['cl'],
    None
)

if __name__ == '__main__':
    plots.make_plot([BaBar_Y3Smu, BaBar_Y2Smu, BaBar_Y1Smu, Belle_Y1Smu, BaBar_Y3Stau, BaBar_Y1Stau, Belle_Y1Stau, BESIII_Jpsimu, BelleII_Y4S3g_lfu], 'quarkonia_lfu.pdf', r'\ell', 'Quarkonia decays (LFU leptophilic ALP)', legend=True, limx=(1e-1, 20), legend_args={'fontsize': 12, 'ncols': 2, 'loc': 'lower left'})
    plots.make_plot([BaBar_Y3Stau, BaBar_Y1Stau, Belle_Y1Stau, BelleII_Y4S3g_tau, BESIII_Jpsi3g_tau], 'quarkonia_tau.pdf', r'\tau', r'Quarkonia decays ($\tau$-philic ALP)', legend=True, limx=(1e-1, 20), legend_args={'fontsize': 14, 'loc': 'lower left'})