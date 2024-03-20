import plots
import pandas as pd

df_invisible = pd.read_csv('../data/meson_lept/invisible_tau.csv')
df_pienua_displaced = pd.read_csv('../data/meson_lept/pienua_displaced.csv')
df_visible = pd.read_csv('../data/meson_lept/visible.csv')

invisible_Btau = plots.PlotData(
    r'$B^+\to\tau^+\nu_\tau a$',
    'g',
    (1,1),
    True,
    df_invisible['ma_GeV'],
    df_invisible['ctau_Blnua'],
    None,
    False
)

invisible_Dtau = plots.PlotData(
    r'$D^+\to\tau^+\nu_\tau a$',
    'r',
    (1,1),
    True,
    df_invisible['ma_GeV'],
    df_invisible['ctau_Dlnua'],
    None,
    False
)

invisible_Dstau = plots.PlotData(
    r'$D_s^+\to\tau^+\nu_\tau a$',
    'b',
    (1,1),
    True,
    df_invisible['ma_GeV'],
    df_invisible['ctau_Dslnua'],
    None,
    False
)

pienua_displaced = plots.PlotData(
    r'$\pi^+ \to e^+ \nu a(\to e^+ e^-)$',
    'tab:blue',
    (2e-3, 1e2),
    True,
    df_pienua_displaced['ma_GeV'],
    df_pienua_displaced['cl_inf'],
    df_pienua_displaced['cl_sup'],
)

visible_Klee = plots.PlotData(
    r'$K^+\to \ell^+ \nu_\ell e^+ e^-$',
    'tab:orange',
    (1e-2, 2),
    True,
    df_visible['ma_GeV'],
    df_visible['cl_Keee'],
    None
)

visible_Kemumu = plots.PlotData(
    r'$K^+\to e^+ \nu_e \mu^+ \mu^-$',
    'tab:green',
    (0.27, 10),
    True,
    df_visible['ma_GeV'],
    df_visible['cl_Kemumu'],
    None
)

visible_Kmumumu = plots.PlotData(
    r'$K^+\to \mu^+ \nu_\mu \mu^+ \mu^-$',
    'tab:red',
    (0.4, 4e2),
    True,
    df_visible['ma_GeV'],
    df_visible['cl_Kmumumu'],
    None
)

visible_Bmumumu = plots.PlotData(
    r'$B^+\to \mu^+ \nu_\mu \mu^+ \mu^-$',
    'tab:purple',
    (0.5, 70),
    True,
    df_visible['ma_GeV'],
    df_visible['cl_Bmumumu'],
    None
)

if __name__ == '__main__':
    plots.make_plot([invisible_Btau, invisible_Dstau, invisible_Dtau], 'meson_lept_invisible.pdf', r'\tau', limx=(1e-3, 3), limy=(10, 1e4), legend=True)
    plots.make_plot([pienua_displaced, visible_Klee, visible_Kemumu, visible_Kmumumu, visible_Bmumumu], 'meson_lept_visible.pdf', r'\ell', limx=(1e-3, 3), limy=(1, 1e4))