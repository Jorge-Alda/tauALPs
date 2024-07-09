import plots

from g2 import BelleII_g2tau_tau
from direct_searches import gammainv, ee3gamma, eetaugamma, gammainv_proj, ee3gamma_proj, eetaugamma_proj
from astro_cosmo import sn_gamma_tau, sn_nu_tau, sn_pvo_tau, sne_tau, gw_fermi_tau, gw_fireball_tau


BelleII_g2tau_tau.textpos = (1.6,15)
BelleII_g2tau_tau.name = r'$(g-2)_\tau$'
gammainv.color = 'brown'
gammainv.textpos = (1.2e-3, 4)
gammainv_proj.textpos = (1.2e-3, 0.3)
gammainv_proj.color = 'brown'
eetaugamma.color = 'red'
eetaugamma_proj.color = 'red'
eetaugamma.textpos = (1, 1000)
ee3gamma.color = 'lightsalmon'
ee3gamma.textpos = (0.2, 120)
ee3gamma_proj.color = 'lightsalmon'
ee3gamma_proj.textpos = (0.35, 2)
BelleII_g2tau_tau.color = 'purple'
sne_tau.textpos = (0.5, 1.5e-1)

if __name__ == '__main__':
    plots.make_plot([sn_gamma_tau, sn_nu_tau, sn_pvo_tau, sne_tau, gw_fermi_tau, gw_fireball_tau, BelleII_g2tau_tau, gammainv, ee3gamma, eetaugamma, gammainv_proj, ee3gamma_proj, eetaugamma_proj], 'moneyplot_tau_BII.pdf', r'\tau', limy=(1e-3, 1e4), limx=(1e-3, 10))