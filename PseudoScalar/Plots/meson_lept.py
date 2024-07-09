import plots
import pandas as pd

#df_invisible = pd.read_csv('../data/meson_lept/invisible_tau.csv')
df_pienua_displaced = pd.read_csv('../data/meson_lept/pienua_displaced.csv')
df_B_mu_mumu = pd.read_csv('../data/meson_lept/B_mu_mumu.csv')
df_K_mu_mumu = pd.read_csv('../data/meson_lept/K_mu_mumu.csv')
df_K_e_mumu = pd.read_csv('../data/meson_lept/K_e_mumu.csv')
df_K_mu_ee = pd.read_csv('../data/meson_lept/K_mu_ee.csv')
df_K_e_ee = pd.read_csv('../data/meson_lept/K_e_ee.csv')

df_pienua_displaced_ewv = pd.read_csv('../data/meson_lept/pienua_displaced_ewv.csv')
df_B_mu_mumu_ewv = pd.read_csv('../data/meson_lept/B_mu_mumu_ewv.csv')
df_K_mu_mumu_ewv = pd.read_csv('../data/meson_lept/K_mu_mumu_ewv.csv')
df_K_e_mumu_ewv = pd.read_csv('../data/meson_lept/K_e_mumu_ewv.csv')
df_K_mu_ee_ewv = pd.read_csv('../data/meson_lept/K_mu_ee_ewv.csv')
df_K_e_ee_ewv = pd.read_csv('../data/meson_lept/K_e_ee_ewv.csv')

pienua_displaced = plots.PlotData(
    r'$\pi^+ \to e^+ \nu a(\to e^+ e^-)$',
    'tab:cyan',
    (2e-3, 1e2),
    True,
    df_pienua_displaced['ma_GeV'],
    df_pienua_displaced['cl_inf'],
    df_pienua_displaced['cl_sup'],
)

visible_Keee = plots.PlotData(
    r'$K^+\to e^+ \nu_e e^+ e^-$',
    'tab:orange',
    (1e-2, 500),
    True,
    df_K_e_ee['ma_GeV'],
    df_K_e_ee['cl'],
    None
)

visible_Kmuee = plots.PlotData(
    r'$K^+\to \mu^+ \nu_\mu e^+ e^-$',
    'tab:blue',
    (1e-2, 17),
    True,
    df_K_mu_ee['ma_GeV'],
    df_K_mu_ee['cl'],
    None
)

visible_Kemumu = plots.PlotData(
    r'$K^+\to e^+ \nu_e \mu^+ \mu^-$',
    'tab:green',
    (0.4, 6e3),
    True,
    df_K_e_mumu['ma_GeV'],
    df_K_e_mumu['cl'],
    None
)

visible_Kmumumu = plots.PlotData(
    r'$K^+\to \mu^+ \nu_\mu \mu^+ \mu^-$',
    'tab:red',
    (0.3, 4e2),
    True,
    df_K_mu_mumu['ma_GeV'],
    df_K_mu_mumu['cl'],
    None
)

visible_Bmumumu = plots.PlotData(
    r'$B^+\to \mu^+ \nu_\mu \mu^+ \mu^-$',
    'tab:purple',
    (0.5, 900),
    True,
    df_B_mu_mumu['ma_GeV'],
    df_B_mu_mumu['cl'],
    None
)

## EW violating

pienua_displaced_ewv = plots.PlotData(
    r'$\pi^+ \to e^+ \nu a(\to e^+ e^-)$',
    'tab:blue',
    (2e-3, 1e2),
    True,
    df_pienua_displaced_ewv['ma_GeV'],
    df_pienua_displaced_ewv['cl_inf'],
    df_pienua_displaced_ewv['cl_sup'],
)

visible_Keee_ewv = plots.PlotData(
    r'$K^+\to e^+ \nu_e e^+ e^-$',
    'tab:orange',
    (1e-2, 2),
    True,
    df_K_e_ee_ewv['ma_GeV'],
    df_K_e_ee_ewv['cl'],
    None
)

visible_Kmuee_ewv = plots.PlotData(
    r'$K^+\to \mu^+ \nu_\ell e^+ e^-$',
    'tab:cyan',
    (2e-3, 4),
    True,
    df_K_mu_ee_ewv['ma_GeV'],
    df_K_mu_ee_ewv['cl'],
    None
)

visible_Kemumu_ewv = plots.PlotData(
    r'$K^+\to e^+ \nu_e \mu^+ \mu^-$',
    'tab:green',
    (0.3, 10),
    True,
    df_K_e_mumu_ewv['ma_GeV'],
    df_K_e_mumu_ewv['cl'],
    None
)

visible_Kmumumu_ewv = plots.PlotData(
    r'$K^+\to \mu^+ \nu_\mu \mu^+ \mu^-$',
    'tab:red',
    (5.5e-2, 4e2),
    True,
    df_K_mu_mumu_ewv['ma_GeV'],
    df_K_mu_mumu_ewv['cl'],
    None
)

visible_Bmumumu_ewv = plots.PlotData(
    r'$B^+\to \mu^+ \nu_\mu \mu^+ \mu^-$',
    'tab:purple',
    (0.5, 900),
    True,
    df_B_mu_mumu_ewv['ma_GeV'],
    df_B_mu_mumu_ewv['cl'],
    None
)

if __name__ == '__main__':
    plots.make_plot([pienua_displaced, visible_Keee, visible_Kmuee, visible_Kemumu, visible_Kmumumu, visible_Bmumumu], 'meson_lept_visible.pdf', r'\ell}\chi_{A', limx=(1e-3, 3), limy=(1, 1e4))
    plots.make_plot([pienua_displaced_ewv, visible_Keee_ewv, visible_Kmuee_ewv, visible_Kemumu_ewv, visible_Kmumumu_ewv, visible_Bmumumu_ewv], 'meson_lept_visible_ewv.pdf', r'\ell}\Delta\chi{', limx=(1e-3, 3), limy=(1, 1e4))