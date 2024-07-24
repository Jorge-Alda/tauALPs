import plots

from g2 import BelleII_g2tau, CMS_g2tau
from direct_searches import eetaugamma, eetaugamma_proj ,gammainv_BaBar, ee3gamma_445pb, gammainv_proj, ee3gamma_proj
from astro_cosmo import sn_gamma_tau, sn_nu_tau, sn_pvo_tau, sne_tau, gw_fermi_tau, gw_fireball_tau
from quarkonia import BaBar_Y3Stau, BESIII_3gamma, BESIII_gammainv, BelleII_gammatau


if __name__ == '__main__':
    CMS_g2tau.name = ''
    ee3gamma_445pb.name = ''
    ee3gamma_proj.name = ''
    BESIII_gammainv.name = ''
    BESIII_3gamma.name = ''
    eetaugamma_proj.name = ''
    BaBar_Y3Stau.name = ''
    BelleII_gammatau.name = ''
    gammainv_proj.textpos = (3e-3, 2e-2)
    gammainv_proj.name = r'$e^+e^-\to\gamma +$ inv.' + r' (Belle II 50 ab$^{-1}$)'
    plots.make_plot([
        sn_gamma_tau, sn_nu_tau, sne_tau, gw_fireball_tau,
        BelleII_g2tau, CMS_g2tau, eetaugamma_proj,
        BaBar_Y3Stau, BESIII_3gamma, BESIII_gammainv, BelleII_gammatau,
        ee3gamma_445pb, gammainv_proj, ee3gamma_proj, 
        ], 'moneyplot_scalar.pdf', r'\tau', limy=(1e-9, 10), limx=(1e-3, 10))
    CMS_g2tau.name = r'$(g-2)_\tau$ (CMS)'
    BelleII_g2tau.textpos = (1.1e-1, 5e-3)
    ee3gamma_445pb.name = r'$e^+e^-\to3\gamma$ (Belle II)'
    ee3gamma_proj.name = r'$e^+e^-\to3\gamma$' + '\n' + r'(Belle II 50 ab$^{-1}$)'
    BESIII_gammainv.name = r'$J/\psi\to\gamma + $ inv. (BESIII)'
    BESIII_3gamma.name = r'$J/\psi\to3\gamma$ (BESIII)'
    eetaugamma_proj.name = r'$e^+e^-\to\tau^+\tau^-\gamma\gamma$' + '\n' + r'(Belle II 50 ab$^{-1}$)'
    BaBar_Y3Stau.name = r'$\Upsilon(3S)\to\gamma\tau^+\tau^-$' + '\n(BaBar)'
    BelleII_gammatau.name = r'$e^+e^-\to\gamma\tau^+\tau^-$'+ '\n' + r'(Belle II 50 ab$^{-1}$)'
    gammainv_proj.textpos = (1.2e-1, 2e-2)
    
    plots.make_plot([
        sn_gamma_tau, sn_nu_tau, sne_tau, gw_fireball_tau,
        BelleII_g2tau, CMS_g2tau, eetaugamma_proj,
        BaBar_Y3Stau, BESIII_3gamma, BESIII_gammainv, BelleII_gammatau,
        ee3gamma_445pb, gammainv_proj, ee3gamma_proj, 
        ], 'moneyplot_scalar_zoomed.pdf', r'\tau', limy=(1e-3, 10), limx=(1e-1, 10))