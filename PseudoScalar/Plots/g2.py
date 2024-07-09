import plots
import pandas as pd

df_g2e_Be = pd.read_csv('../data/anomalous_moments/g2e_Be.csv')
df_g2e_Cs = pd.read_csv('../data/anomalous_moments/g2e_Cs.csv')
df_g2e = pd.read_csv('../data/anomalous_moments/g2e.csv')
df_g2mu = pd.read_csv('../data/anomalous_moments/g2mu.csv')
df_g2tau_lfu = pd.read_csv('../data/anomalous_moments/g2tau_lfu.csv')
df_g2_cgg = pd.read_csv('../data/anomalous_moments/g2_cgg.csv')
df_g2_tau_tau = pd.read_csv('../data/anomalous_moments/g2tau_tau.csv')

g2e = plots.PlotData(
    r'$(g-2)_e$',
    'deeppink',
    (1.5e-3, 12),
    True,
    df_g2e['ma_GeV'],
    df_g2e['c_g2e'],
    None
)

g2mu = plots.PlotData(
    r'$(g-2)_\mu$',
    'chocolate',
    (220, 25),
    True,
    df_g2mu['ma_GeV'],
    df_g2mu['c_g2mu'],
    None
)

BelleII_g2tau = plots.PlotData(
    r'$(g-2)_\tau$' + '\n(Belle II)',
    'darkred',
    (1.5e-3, 2.5),
    False,
    df_g2tau_lfu['ma_GeV'],
    df_g2tau_lfu['c_g2tau_BelleII'],
    None
)

ATLAS_g2tau = plots.PlotData(
    r'$(g-2)_\tau$' + '\n(ATLAS, ' + r'$q\bar{q}\to \tau^+\tau^-$)',
    'tab:green',
    (1.5e-3, 100),
    True,
    df_g2tau_lfu['ma_GeV'],
    df_g2tau_lfu['c_g2tau_ATLAS'],
    None
)




CMS24_g2tau = plots.PlotData(
    r'$(g-2)_\tau$' + '\n(CMS, p-p)',
    'tab:red',
    (1e-1, 470),
    True,
    df_g2tau_lfu['ma_GeV'],
    df_g2tau_lfu['c_g2tau_CMS24'],
    None
)



cgg_g2e = plots.PlotDataGauge(
    r'$(g-2)_e$',
    'purple',
    (1.5e-2, 40),
    df_g2_cgg['ma_GeV'],
    df_g2e['c_g2e'],
    df_g2_cgg['cl_g2e+cgg'],
    df_g2_cgg['cl_g2e-cgg'],
)

cgg_g2mu = plots.PlotDataGauge(
    r'$(g-2)_\mu$',
    'tab:blue',
    (1.6, 14),
    df_g2_cgg['ma_GeV'],
    df_g2mu['c_g2mu'],
    df_g2_cgg['cl_g2mu+cgg'],
    df_g2_cgg['cl_g2mu-cgg'],
)

cgg_g2tauATLAS = plots.PlotDataGauge(
    r'$(g-2)_\tau$' + '\n(ATLAS, ' + r'$q\bar{q}\to \tau^+\tau^-$)',
    'tab:green',
    (20, 130),
    df_g2_cgg['ma_GeV'],
    df_g2tau_lfu['c_g2tau_ATLAS'],
    df_g2_cgg['cl_g2tauATLAS+cgg'],
    df_g2_cgg['cl_g2tauATLAS-cgg'],
)

cgg_g2tauBelleII = plots.PlotDataGauge(
    r'$(g-2)_\tau$' + '\n(Belle II)',
    'darkred',
    (30, 2.2),
    df_g2_cgg['ma_GeV'],
    df_g2tau_lfu['c_g2tau_BelleII'],
    df_g2_cgg['cl_g2tauBII+cgg'],
    df_g2_cgg['cl_g2tauBII-cgg'],
)

BelleII_g2tau_tau = plots.PlotData(
    r'$(g-2)_\tau$' + '\n(Belle II)',
    'darkred',
    (1.5e-3, 1.8),
    False,
    df_g2_tau_tau['ma_GeV'],
    df_g2_tau_tau['ctau_BelleII'],
    None
)

ATLAS_g2tau_tau = plots.PlotData(
    r'$(g-2)_\tau$' + '\n(ATLAS, ' + r'$q\bar{q}\to \tau^+\tau^-$)',
    'darkred',
    (5e-3, 250),
    True,
    df_g2_tau_tau['ma_GeV'],
    df_g2_tau_tau['ctau_ATLAS'],
    None
)

if __name__ == '__main__':
    g2e.color = 'purple'
    plots.make_plot([g2e, BelleII_g2tau, ATLAS_g2tau, CMS24_g2tau], 'g2_lfu.pdf', r'\ell', limy=(1, 1e4))
    plots.make_plot([
        cgg_g2e,
        cgg_g2mu,
        cgg_g2tauATLAS,
        cgg_g2tauBelleII
    ], 'g2_cgg.pdf', r'\ell', r'$(g-2)_\ell$, $c_{\gamma\gamma}^0\in [-5, +5] c_\ell$, $c_{\gamma Z}^0 = 0$',  limy=(1, 1e4))