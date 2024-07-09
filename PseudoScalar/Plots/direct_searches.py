import plots
import pandas as pd

fa = 1000
vev = 246

df_Belle_tautauALP = pd.read_csv('../data/direct_searches/direct_Belle.dat', sep='\t')
df_BelleII_tautauALP = pd.read_csv('../data/direct_searches/direct_BelleII.dat', sep='\t')
df_BelleII_mumuALP = pd.read_csv('../data/direct_searches/BelleII_taures.csv')
df_BaBar_gammaALP = pd.read_csv('../data/direct_searches/BaBar_darkphoton_N.csv', names=['ma_GeV', 'cl'], sep=' ').sort_values(by='ma_GeV')
df_gammainv_inf = pd.read_csv('../data/direct_searches/gammainv_inf.csv')
df_gammainv_proj = pd.read_csv('../data/direct_searches/gammainv_proj.csv')
df_ee3gamma = pd.read_csv('../data/direct_searches/ee3gamma.csv')
df_ee3gamma_proj = pd.read_csv('../data/direct_searches/ee3gamma_proj.csv')
df_eetaugamma = pd.read_csv('../data/direct_searches/eetaugamma.csv')
df_eetaugamma_proj = pd.read_csv('../data/direct_searches/eetaugamma_proj.csv')

Belle_tautauALP = plots.PlotData(
    r'$e^+e^-\to \tau^+\tau^- \ell^+\ell^-$' + '\n(Belle)',
    'purple',
    (0.2, 4.8),
    True,
    df_Belle_tautauALP['ma_GeV'],
    df_Belle_tautauALP['xitau_direct_Belle']*fa/vev,
    None
)

BelleII_tautauALP = plots.PlotData(
    r'$e^+e^-\to \tau^+\tau^- a$' + '\n(Belle II)',
    'darkolivegreen',
    (2e-2, 0.3),
    False,
    df_BelleII_tautauALP['ma_GeV'],
    df_BelleII_tautauALP['xitau_BelleII']*fa/vev,
    None
)

BelleII_mumuALP = plots.PlotData(
    r'$e^+e^-\to \mu^+\mu^- a$' + '\n(Belle II)',
    'deeppink',
    (2, 7e3),
    True,
    df_BelleII_mumuALP['m [GeV/c^2]'],
    df_BelleII_mumuALP[r' {c_{\ell\ell}/\Lambda}_UL_obs [TeV^-1]'],
    None
)

BaBar_gammaALP = plots.PlotData(
    r'$e^+e^-\to \gamma a$' + '\n(BaBar)',
    'tab:blue',
    (0.4, 250),
    True,
    df_BaBar_gammaALP['ma_GeV'],
    df_BaBar_gammaALP['cl'],
    None
)

gammainv = plots.PlotData(
    r'$e^+e^-\to \gamma +$ inv',
    'slategray',
    (3e-3, 12),
    True,
    df_gammainv_inf['ma_GeV'],
    df_gammainv_inf['cl_inf'],
    df_gammainv_inf['cl_sup']
)

gammainv_proj = plots.PlotData(
    r'$e^+e^-\to \gamma +$ inv' + '\n' + r'  (50 ab$^{-1}$)',
    'slategray',
    (3e-3, 1.6),
    False,
    df_gammainv_proj['ma_GeV'],
    df_gammainv_proj['cl_inf'],
    df_gammainv_proj['cl_sup']
)

ee3gamma = plots.PlotData(
    r'$e^+e^-\to 3\gamma$',
    'teal',
    (3e-2, 80),
    True,
    df_ee3gamma['ma_GeV'],
    df_ee3gamma['cl'],
    None
)

ee3gamma_proj = plots.PlotData(
    r'$e^+e^-\to 3\gamma$' +'\n' + r'(50 ab$^{-1}$)',
    'teal',
    (13e-2, 2),
    False,
    df_ee3gamma_proj['ma_GeV'],
    df_ee3gamma_proj['cl'],
    None
)

eetaugamma = plots.PlotData(
    r'$e^+e^-\to \tau^+\tau^-\gamma\gamma$',
    'purple',
    (3.4, 40),
    True,
    df_eetaugamma['ma_GeV'],
    df_eetaugamma['cl'],
    None
)

eetaugamma_proj = plots.PlotData(
    r'$e^+e^-\to \tau^+\tau^-\gamma\gamma$' + '\n' + r'(50 ab$^{-1}$)',
    'purple',
    (1, 1),
    False,
    df_eetaugamma_proj['ma_GeV'],
    df_eetaugamma_proj['cl'],
    None
)

if __name__ == '__main__':
    plots.make_plot([Belle_tautauALP, BelleII_tautauALP, BelleII_mumuALP, BaBar_gammaALP], 'direct_searches.pdf', r'\ell')