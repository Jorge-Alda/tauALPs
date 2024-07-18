import plots

from g2 import BelleII_g2tau, ATLAS_g2tau
from direct_searches import eetaugamma, eetaugamma_proj ,gammainv_BaBar, ee3gamma_445pb, gammainv_proj, ee3gamma_proj
from astro_cosmo import sn_gamma_tau, sn_nu_tau, sn_pvo_tau, sne_tau, gw_fermi_tau, gw_fireball_tau


if __name__ == '__main__':
    plots.make_plot([
        sn_gamma_tau, sn_nu_tau, sne_tau, gw_fireball_tau,
        BelleII_g2tau, ATLAS_g2tau, eetaugamma_proj,
        gammainv_BaBar, ee3gamma_445pb, gammainv_proj, ee3gamma_proj, 
        ], 'moneyplot_scalar.pdf', r'\tau', limy=(1e-9, 10), limx=(1e-3, 10))