import plots
import pandas as pd

df_g2e_Be = pd.read_csv('../data/anomalous_moments/g2e_Be.csv')
df_g2e_Cs = pd.read_csv('../data/anomalous_moments/g2e_Cs.csv')
df_g2e = pd.read_csv('../data/anomalous_moments/g2e.csv')
df_g2mu = pd.read_csv('../data/anomalous_moments/g2mu.csv')
df_g2tau_lfu = pd.read_csv('../data/anomalous_moments/g2tau_lfu.csv')
df_g2_cgg = pd.read_csv('../data/anomalous_moments/g2_cgg.csv')

g2e = plots.PlotData(
    r'$(g-2)_e$',
    'darkgray',
    (1.5e-3, 20),
    True,
    df_g2e['ma_GeV'],
    df_g2e['cl_g2e'],
    None
)

g2e_Be = plots.PlotData(
    r'$(g-2)_e$ ${}^8$Be',
    'darkgray',
    (1.5e-2, 40),
    True,
    df_g2e_Be['ma_GeV'],
    df_g2e_Be['c_g2e'],
    None
)

g2e_Cs = plots.PlotData(
    r'$(g-2)_e$ ${}^{133}$Cs',
    'k',
    (1.2e-3, 50),
    True,
    df_g2e_Cs['ma_GeV'],
    df_g2e_Cs['c_g2e'],
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
    (1.5e-3, 4.2),
    False,
    df_g2tau_lfu['ma_GeV'],
    df_g2tau_lfu['c_g2tau_BelleII'],
    None
)

ATLAS_g2tau = plots.PlotData(
    r'$(g-2)_\tau$' + '\n(ATLAS, ' + r'$q\bar{q}\to \tau^+\tau^-$)',
    'tab:green',
    (5e-3, 250),
    True,
    df_g2tau_lfu['ma_GeV'],
    df_g2tau_lfu['c_g2tau_ATLAS'],
    None
)

ATLASPb_g2tau = plots.PlotData(
    r'$(g-2)_\tau$' + '\n(ATLAS, Pb-Pb)',
    'tab:orange',
    (1e-1, 600),
    True,
    df_g2tau_lfu['ma_GeV'],
    df_g2tau_lfu['c_g2tau_ATLASPb'],
    None
)

CMS_g2tau = plots.PlotData(
    r'$(g-2)_\tau$' + '\n(CMS, Pb-Pb)',
    'tab:blue',
    (5e-3, 3e3),
    True,
    df_g2tau_lfu['ma_GeV'],
    df_g2tau_lfu['c_g2tau_CMS'],
    None
)

cgg_g2e = plots.PlotDataGauge(
    r'$(g-2)_e$',
    'darkgray',
    (1.5e-1, 1e2),
    df_g2_cgg['ma_GeV'],
    df_g2e['cl_g2e'],
    df_g2_cgg['cl_g2e+cgg'],
    df_g2_cgg['cl_g2e-cgg'],
)

cgg_g2mu = plots.PlotDataGauge(
    r'$(g-2)_\mu$',
    'chocolate',
    (0.6, 14),
    df_g2_cgg['ma_GeV'],
    df_g2mu['c_g2mu'],
    df_g2_cgg['cl_g2mu+cgg'],
    df_g2_cgg['cl_g2mu-cgg'],
)

cgg_g2tauATLAS = plots.PlotDataGauge(
    r'$(g-2)_\tau$' + '\n(ATLAS, ' + r'$q\bar{q}\to \tau^+\tau^-$)',
    'tab:green',
    (1.6, 200),
    df_g2_cgg['ma_GeV'],
    df_g2tau_lfu['c_g2tau_ATLAS'],
    df_g2_cgg['cl_g2tauATLAS+cgg'],
    df_g2_cgg['cl_g2tauATLAS-cgg'],
)

cgg_g2tauBelleII = plots.PlotDataGauge(
    r'$(g-2)_\tau$' + '\n(Belle II)',
    'darkred',
    (30, 7),
    df_g2_cgg['ma_GeV'],
    df_g2tau_lfu['c_g2tau_BelleII'],
    df_g2_cgg['cl_g2tauBII+cgg'],
    df_g2_cgg['cl_g2tauBII-cgg'],
)

if __name__ == '__main__':
    plots.make_plot([g2e, g2mu, BelleII_g2tau, ATLAS_g2tau, ATLASPb_g2tau, CMS_g2tau], 'g2_lfu.pdf', r'\ell', r'$(g-2)_\ell$, Leptophilic LFU ALP')
    plots.make_plot([cgg_g2e, cgg_g2mu, cgg_g2tauATLAS, cgg_g2tauBelleII], 'g2_cgg.pdf', r'\ell', r'$(g-2)_\ell$, $c_{\gamma\gamma}^0\in [-5, +5] c_\ell$, $c_{\gamma Z}^0 = 0$', limx=(1e-1, 1e3), limy=(1, 1e4))