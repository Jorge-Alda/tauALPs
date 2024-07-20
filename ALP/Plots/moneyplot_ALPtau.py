import plots

from g2 import BelleII_g2tau_tau, ATLAS_g2tau_tau
from direct_searches import gammainv_BaBar, ee3gamma_445pb, eetaugamma, gammainv_proj, ee3gamma_proj, eetaugamma_proj
from astro_cosmo import sn_gamma_tau, sn_nu_tau, sn_pvo_tau, sne_tau, gw_fermi_tau, gw_fireball_tau


BelleII_g2tau_tau.textpos = (1.2e-3,9)
BelleII_g2tau_tau.name = r'$(g-2)_\tau$ (Belle II)'
gammainv_BaBar.color = 'brown'
gammainv_BaBar.textpos = (1.2e-3, 30)
gammainv_proj.textpos = (1.2e-3, 0.5)
gammainv_proj.color = 'brown'
eetaugamma.color = 'xkcd:pumpkin orange'
eetaugamma_proj.color = 'xkcd:pumpkin orange'
eetaugamma.textpos = (1.2, 40)
eetaugamma_proj.textpos = (1.4, 0.6)
ee3gamma_445pb.color = 'red'
ee3gamma_445pb.textpos = (2, 190)
ee3gamma_proj.color = 'red'
ee3gamma_proj.textpos = (2, 9.77)
BelleII_g2tau_tau.color = 'purple'
sne_tau.textpos = (0.5, 1.5e-1)
sn_nu_tau.textpos = (0.35, 0.4)
ATLAS_g2tau_tau.color = 'purple'
ATLAS_g2tau_tau.textpos = (1.2e-3, 170)

if __name__ == '__main__':
    plots.make_plot_tau([sn_gamma_tau, sn_nu_tau, sne_tau, gw_fireball_tau, BelleII_g2tau_tau, ATLAS_g2tau_tau, gammainv_BaBar, gammainv_proj, ee3gamma_445pb, ee3gamma_proj, eetaugamma_proj], 'moneyplot_ALPtau.pdf', limy=(1e-9, 10), limx=(1e-3, 10))