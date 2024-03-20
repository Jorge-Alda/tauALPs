import plots
from astro_cosmo import sn1987a
from displacedv import LHCb_combined
from quarkonia import BaBar_Y3Stot
from direct_searches import Belle_tautauALP, BelleII_tautauALP
from g2 import g2e, g2mu, BelleII_g2tau

if __name__ == '__main__':
    plots.make_plot([sn1987a, LHCb_combined, BaBar_Y3Stot, Belle_tautauALP, BelleII_tautauALP, g2e, g2mu, BelleII_g2tau], 'moneyplot_lfu.pdf', r'\ell', 'LFU leptophilic ALP')