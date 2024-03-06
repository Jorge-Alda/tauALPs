import plots
from astro_cosmo import sn1987a
from displacedv import LHCb_combined
from quarkonia import BaBar_Y3Stot

if __name__ == '__main__':
    plots.make_plot([sn1987a, LHCb_combined, BaBar_Y3Stot], 'moneyplot_lfu.pdf', r'\ell', 'LFU leptophilic ALP')