import plots
from astro_cosmo import sn1987a
from displacedv import LHCb_combined

if __name__ == '__main__':
    plots.make_plot([sn1987a, LHCb_combined], 'moneyplot_lfu.pdf', r'\ell', 'LFU leptophilic ALP')