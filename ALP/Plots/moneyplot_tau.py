import plots

from meson_semilep import Kpiinv_tau, BKinv_tau, Bstautau
from quarkonia import BaBar_Y3Stau
from g2 import BelleII_g2tau_tau, ATLAS_g2tau_tau
from direct_searches import gammainv, ee3gamma, eetaugamma, gammainv_proj, ee3gamma_proj, eetaugamma_proj
from displacedv import BaBar_BKa
from beamdump import beamdump_photons_tau

import pandas as pd
higgs_data = pd.read_csv('../data/higgs.csv')
ppWa_data = pd.read_csv('../data/ppWa_tau.csv')
df_lblPb = pd.read_csv('../data/astro_cosmo/ATLAS_PbPb.csv')

higgs = plots.PlotData(
    r'$h \to$ BSM',
    'tab:cyan',
    (6, 190),
    True,
    higgs_data['ma_GeV'],
    higgs_data['cl'],
    None
)

ppWa = plots.PlotData(
    r'$pp\to W \tau^+\tau^-$',
    'blueviolet',
    (32, 85),
    True,
    ppWa_data['ma_GeV'],
    ppWa_data['ctau'],
    None
)

lblPb = plots.PlotData(
    r'$\gamma\gamma\to\gamma\gamma$ (Pb)',
    'olive',
    (30, 1000),
    True,
    df_lblPb['ma_GeV'],
    df_lblPb['ctau'],
    None
)

ATLAS_g2tau_tau.textpos = (1.5e-3, 245)
BelleII_g2tau_tau.textpos = (80,20)
BaBar_BKa.textpos = (2.5, 5)
BaBar_BKa.name = r"$B\to K a(\to \gamma\gamma)$"
BaBar_BKa.color = "r"

if __name__ == '__main__':
    plots.make_plot([Bstautau, higgs, Kpiinv_tau, BKinv_tau, BaBar_Y3Stau, BelleII_g2tau_tau, ATLAS_g2tau_tau, gammainv, ee3gamma, eetaugamma, ppWa, BaBar_BKa, gammainv_proj, ee3gamma_proj, eetaugamma_proj, lblPb, beamdump_photons_tau], 'moneyplot_tau.pdf', r'\tau', 'Tauphilic ALP', limy=(1e-1, 1e4), limx=(1e-3, 300))