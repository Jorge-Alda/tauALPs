import plots
import pandas as pd

df_sn_gamma = pd.read_csv('../data/astro_cosmo/sn_gamma.csv')
df_sn_nu = pd.read_csv('../data/astro_cosmo/sn_nu.csv')
df_sn_pvo = pd.read_csv('../data/astro_cosmo/sn_pvo.csv')
df_sne = pd.read_csv('../data/astro_cosmo/sne.csv')
df_gw_fermi = pd.read_csv('../data/astro_cosmo/gw_fermi.csv')
df_gw_fireball = pd.read_csv('../data/astro_cosmo/gw_fireball.csv')


sn_gamma_lfu = plots.PlotDataClosed(
    'SN 1987A\n' + r'$\gamma$ ray burst',
    'forestgreen',
    (2e-3, 3e-7),
    True,
    df_sn_gamma['ma_GeV'],
    df_sn_gamma['gl'],
)

sn_nu_lfu = plots.PlotDataClosed(
    'SN 1987A\n' + r'$\nu$ signal',
    'yellowgreen',
    (1e-2, 1),
    True,
    df_sn_nu['ma_GeV'],
    df_sn_nu['gl'],
)

sn_pvo_lfu = plots.PlotDataClosed(
    'SN 1987A\n' + r'Pioneer Venus Orbiter',
    'teal',
    (1e-2, 2e2),
    True,
    df_sn_pvo['ma_GeV'],
    df_sn_pvo['gl'],
)

sne_lfu = plots.PlotDataClosed(
    'Low energy SN',
    'lightgreen',
    (0.3, 3.5e-3),
    True,
    df_sne['ma_GeV'],
    df_sne['gl'],
)

gw_fermi_lfu = plots.PlotDataClosed(
    'GW170817\nFermi',
    'navy',
    (2e-3, 0.55e-4),
    True,
    df_gw_fermi['ma_GeV'],
    df_gw_fermi['gl'],
)


gw_fireball_lfu = plots.PlotDataClosed(
    'GW170817\nFireball',
    'deepskyblue',
    (0.35, 1e-5),
    True,
    df_gw_fireball['ma_GeV'],
    df_gw_fireball['gl'],
)

###### Tau-philic

sn_gamma_tau = plots.PlotDataClosed(
    'SN 1987A\n' + r'$\gamma$ ray burst',
    'forestgreen',
    (2e-2, 1e-8),
    True,
    df_sn_gamma['ma_GeV'],
    df_sn_gamma['gtau'],
)

sn_nu_tau = plots.PlotDataClosed(
    'SN 1987A\n' + r'$\nu$ signal',
    'yellowgreen',
    (2e-3, 1e-3),
    True,
    df_sn_nu['ma_GeV'],
    df_sn_nu['gtau'],
)

sn_pvo_tau = plots.PlotDataClosed(
    'SN 1987A\n' + r'Pioneer Venus Orbiter',
    'teal',
    (1e-2, 2e2),
    True,
    df_sn_pvo['ma_GeV'],
    df_sn_pvo['gtau'],
)

sne_tau = plots.PlotDataClosed(
    'Low energy SN',
    'lightgreen',
    (0.52, 3e-6),
    True,
    df_sne['ma_GeV'],
    df_sne['gtau'],
)

gw_fermi_tau = plots.PlotDataClosed(
    'GW170817\nFermi',
    'navy',
    (0.6e-2, 2e-1),
    True,
    df_gw_fermi['ma_GeV'],
    df_gw_fermi['gtau'],
)


gw_fireball_tau = plots.PlotDataClosed(
    'GW170817\nFireball',
    'deepskyblue',
    (0.4, 4e-8),
    True,
    df_gw_fireball['ma_GeV'],
    df_gw_fireball['gtau'],
)

if __name__ == '__main__':
    plots.make_plot([sn_gamma_lfu, sn_nu_lfu, sn_pvo_lfu, sne_lfu, gw_fermi_lfu, gw_fireball_lfu], 'astro_cosmo.pdf', r'\ell', limy=(1e-7, 10), limx=(1e-3, 1))
    plots.make_plot([sn_gamma_tau, sn_nu_tau, sn_pvo_tau, sne_tau, gw_fermi_tau, gw_fireball_tau], 'astro_cosmo_tau.pdf', r'\tau', limy=(1e-6, 1e4), limx=(1e-3, 1))