import plots
import pandas as pd

df_LHCb_BKa = pd.read_csv('../data/displacedv/LHCb_BKa.csv')
df_LHCb_combined = pd.read_csv('../data/displacedv/LHCb_combined.csv')
df_LHCb_BKsa = pd.read_csv('../data/displacedv/LHCb_BKsa.csv')
df_BelleII_BKa = pd.read_csv('../data/displacedv/BelleII_BKa.csv')
df_BaBar_BKa = pd.read_csv('../data/displacedv/BaBar_BKa.csv')

LHCb_BKa = plots.PlotData(
    r'$B^+\to K^+ a(\to \mu^+\mu^-)$' + '\n(LHCb)',
    'r',
    (7e-2, 0.2),
    True,
    df_LHCb_BKa['ma_GeV'],
    df_LHCb_BKa['cl_inf'],
    df_LHCb_BKa['cl_sup']
)

LHCb_BKsa = plots.PlotData(
    r'$B^0\to K^{*0} a(\to \mu^+\mu^-)$' + '\n(LHCb)',
    'b',
    (1.4, 0.2),
    True,
    df_LHCb_BKsa['ma_GeV'],
    df_LHCb_BKsa['cl_inf'],
    df_LHCb_BKsa['cl_sup']
)

LHCb_combined = plots.PlotData(
    r'$B\to K^{(*)} a(\to \mu^+\mu^-)$' + '\n(LHCb)',
    'r',
    (7e-2, 0.2),
    True,
    df_LHCb_combined['ma_GeV'],
    df_LHCb_combined['cl_inf'],
    df_LHCb_combined['cl_sup']
)

BelleII_BKa = plots.PlotData(
    r'$B\to K^{(*)} a(\to e^+e^-)$' + '\n(Belle II)',
    'tab:green',
    (1e-2, 40),
    True,
    df_BelleII_BKa['ma_GeV'],
    df_BelleII_BKa['cl_inf'],
    df_BelleII_BKa['cl_sup']
)

BaBar_BKa = plots.PlotData(
    r'$B^\pm\to K^\pm a(\to \gamma\gamma)$' + '\n(BaBar)',
    'tab:orange',
    (1.5, 80),
    True,
    df_BaBar_BKa['ma_GeV'],
    df_BaBar_BKa['cl_inf'],
    df_BaBar_BKa['cl_sup']
)

if __name__ == '__main__':
    plots.make_plot([LHCb_BKsa, LHCb_BKa, BelleII_BKa, BaBar_BKa], 'displacedv.pdf', r'\ell', r'$B\to K a$ with displaced vertex')