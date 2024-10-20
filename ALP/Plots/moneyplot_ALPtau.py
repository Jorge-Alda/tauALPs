import plots

from g2 import BelleII_g2tau_tau, CMS_g2tau_tau
from direct_searches import gammainv_BaBar, ee3gamma_445pb, eetaugamma, gammainv_proj, ee3gamma_proj, eetaugamma_proj
from astro_cosmo import sn_gamma_tau, sn_nu_tau, sn_pvo_tau, sne_tau, gw_fermi_tau, gw_fireball_tau, sn_explo_tau
from quarkonia import BaBar_Y3Stau, BESIII_3gamma, BESIII_gammainv, BelleII_gammatau
from beamdump import beamdump_photons_tau

BelleII_g2tau_tau.textpos = (1.2e-3,9)
BelleII_g2tau_tau.name = r'$(g-2)_\tau$ (Belle II)'
gammainv_BaBar.color = 'brown'
gammainv_BaBar.textpos = (1.2e-3, 30)
gammainv_proj.textpos = (1.2e-3, 1.3)
gammainv_proj.color = 'brown'
eetaugamma.color = 'xkcd:pumpkin orange'
eetaugamma_proj.color = 'xkcd:pumpkin orange'
eetaugamma.textpos = (1.2, 40)
eetaugamma_proj.textpos = (1.4, 0.6)
ee3gamma_445pb.color = 'red'
ee3gamma_445pb.textpos = (2, 190)
ee3gamma_proj.color = 'red'
ee3gamma_proj.textpos = (1.1, 4)
BelleII_g2tau_tau.color = 'purple'
sne_tau.textpos = (0.5, 1.5e-1)
sn_nu_tau.textpos = (0.35, 0.4)
CMS_g2tau_tau.color = 'purple'

if __name__ == '__main__':
    CMS_g2tau_tau.name = ''
    ee3gamma_445pb.name = ''
    ee3gamma_proj.name = ''
    BESIII_gammainv.name = ''
    BESIII_3gamma.name = ''
    eetaugamma_proj.name = ''
    BaBar_Y3Stau.name = ''
    BelleII_gammatau.name = ''
    beamdump_photons_tau.name = ''
    gammainv_proj.name = r'$e^+e^-\to\gamma +$ inv.' + r' (Belle II 50 ab$^{-1}$)'
    plots.make_plot_tau([sn_explo_tau, sn_gamma_tau, sn_nu_tau, sne_tau, gw_fireball_tau, BelleII_g2tau_tau, CMS_g2tau_tau, gammainv_proj, ee3gamma_445pb, ee3gamma_proj, eetaugamma_proj, 
        BaBar_Y3Stau, BESIII_3gamma, BESIII_gammainv, BelleII_gammatau, beamdump_photons_tau], 'moneyplot_ALPtau.pdf', limy=(1e-9, 10), limx=(1e-3, 10))
    CMS_g2tau_tau.name = r'$(g-2)_\tau$ (CMS)'
    BelleII_g2tau_tau.textpos = (1.1e-1, 1.5e-2)
    ee3gamma_445pb.name = r'$e^+e^-\to3\gamma$ (Belle II)'
    ee3gamma_proj.name = r'$e^+e^-\to3\gamma$' + '\n' + r'(Belle II 50 ab$^{-1}$)'
    BESIII_gammainv.name = r'$J/\psi\to\gamma + $ inv. (BESIII)'
    BESIII_3gamma.name = r'$J/\psi\to3\gamma$ (BESIII)'
    eetaugamma_proj.name = r'$e^+e^-\to\tau^+\tau^-\gamma\gamma$' + '\n' + r'(Belle II 50 ab$^{-1}$)'
    BaBar_Y3Stau.name = r'$\Upsilon(3S)\to\gamma\tau^+\tau^-$' + '\n(BaBar)'
    BelleII_gammatau.name = r'$e^+e^-\to\gamma\tau^+\tau^-$'+ '\n' + r'(Belle II 50 ab$^{-1}$)'
    beamdump_photons_tau.name = 'Beam dump'
    beamdump_photons_tau.textpos = (1.16e-1,50)
    BelleII_g2tau_tau.textpos = (1.2e-1,9)
    CMS_g2tau_tau.textpos = (1.1e-1,280)
    gammainv_proj.textpos = (1.2e-1, 3.3)
    eetaugamma_proj.textpos = (1.1, 0.9)
    ee3gamma_proj.textpos = (1.3, 32)
    ee3gamma_445pb.textpos = (1.0, 900)
    BaBar_Y3Stau.textpos = (2, 1.6e-1)
    plots.make_plot_tau([BelleII_g2tau_tau, CMS_g2tau_tau, gammainv_proj, ee3gamma_445pb, ee3gamma_proj, eetaugamma_proj, 
        BaBar_Y3Stau, BESIII_3gamma, BESIII_gammainv, BelleII_gammatau, beamdump_photons_tau], 'moneyplot_ALPtau_zoomed.pdf', limy=(1e-3, 10), limx=(1e-1, 10))