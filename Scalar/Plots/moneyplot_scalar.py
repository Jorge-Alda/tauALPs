import plots

from g2 import BelleII_g2tau, ATLAS_g2tau
from direct_searches import eetaugamma, eetaugamma_proj #,gammainv, ee3gamma, gammainv_proj, ee3gamma_proj, 
from astro_cosmo import sn_gamma_tau, sn_nu_tau, sn_pvo_tau, sne_tau, gw_fermi_tau, gw_fireball_tau


""" gammainv.color = 'brown'
gammainv.textpos = (1.2e-3, 11)
gammainv_proj.textpos = (1.2e-3, 0.36)
gammainv_proj.color = 'brown'
ee3gamma.color = 'lightsalmon'
ee3gamma.textpos = (0.2, 90)
ee3gamma_proj.color = 'lightsalmon'
ee3gamma_proj.textpos = (0.35, 2) """

if __name__ == '__main__':
    plots.make_plot([
        sn_gamma_tau, sn_nu_tau, sne_tau, gw_fireball_tau,
        BelleII_g2tau, ATLAS_g2tau,
        eetaugamma, eetaugamma_proj,
        #gammainv, ee3gamma, , gammainv_proj, ee3gamma_proj, 
        ], 'moneyplot_scalar.pdf', r'\tau', limy=(1e-6, 1e3), limx=(1e-3, 10))