import plots
from astro_cosmo import sn1987a
from displacedv import LHCb_combined
from quarkonia import BaBar_Y3Stot
from direct_searches import Belle_tautauALP, BelleII_tautauALP
from g2 import g2e, g2mu, BelleII_g2tau
from beamdump import beamdump_combined, beamdump_photons
from meson_lept import visible_Kmuee
from meson_semilep import Kpiinv, BKmumu, Bsmumu

import pandas as pd
higgs_data = pd.read_csv('../data/higgs.csv')
ppWa_data = pd.read_csv('../data/ppWa.csv')
df_lblPb = pd.read_csv('../data/astro_cosmo/ATLAS_PbPb.csv')

higgs = plots.PlotData(
    r'$h \to$ BSM',
    'tab:cyan',
    (6, 100),
    True,
    higgs_data['ma_GeV'],
    higgs_data['cl'],
    None
)

ppWa = plots.PlotData(
    r'$pp\to W \tau^+\tau^-$',
    'blueviolet',
    (18, 30),
    True,
    ppWa_data['ma_GeV'],
    ppWa_data['cl'],
    None
)

lblPb = plots.PlotData(
    r'$\gamma\gamma\to\gamma\gamma$ (Pb)',
    'olive',
    (11, 800),
    True,
    df_lblPb['ma_GeV'],
    df_lblPb['cl'],
    None
)


BaBar_Y3Stot.name = r'$\Upsilon(3S)\to\gamma\ell^+\ell^-$'
Belle_tautauALP.name = r'$e^+e^- \to \tau^+\tau^-\ell^+\ell^-$'
Belle_tautauALP.textpos = (0.1, 3.8)
LHCb_combined.name = r'$B\to K^{(*)}a(\to\mu^+\mu^-)$'
BelleII_g2tau.textpos = (9,5)

if __name__ == '__main__':
    plots.make_plot([Bsmumu, sn1987a, beamdump_combined, beamdump_photons, LHCb_combined, BaBar_Y3Stot, Belle_tautauALP, g2e, BelleII_g2tau, visible_Kmuee, higgs, ppWa, Kpiinv, BKmumu, lblPb], 'moneyplot_lfu.pdf', r'\ell', 'LFU leptophilic ALP', limy=(1e-3, 1e4), limx=(1e-3, 300))