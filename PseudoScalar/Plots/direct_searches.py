import plots
import pandas as pd

fa = 1000
vev = 246

df_Belle_tautauALP = pd.read_csv('../data/direct_searches/direct_Belle.dat', sep='\t')
df_BelleII_tautauALP = pd.read_csv('../data/direct_searches/direct_BelleII.dat', sep='\t')
df_BelleII_mumuALP = pd.read_csv('../data/direct_searches/BelleII_taures.csv')
df_BaBar_gammaALP = pd.read_csv('../data/direct_searches/BaBar_darkphoton_N.csv', names=['ma_GeV', 'cl'], sep=' ').sort_values(by='ma_GeV')

Belle_tautauALP = plots.PlotData(
    r'$e^+e^-\to \tau^+\tau^- a$' + '\n(Belle)',
    'purple',
    (0.6e-1, 4.8),
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

if __name__ == '__main__':
    plots.make_plot([Belle_tautauALP, BelleII_tautauALP, BelleII_mumuALP, BaBar_gammaALP], 'direct_searches.pdf', r'\ell')