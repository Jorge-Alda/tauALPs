import plots
import pandas as pd

df_Kpiinv = pd.read_csv("../data/meson_semilep/Kpiinv.csv")
df_Kpiinv.cl.replace(0, float('nan'), inplace=True)
df_BKmumu = pd.read_csv("../data/meson_semilep/BKmumu.csv")
df_BKmumu.cl.replace(0, float('nan'), inplace=True)
df_BKinv = pd.read_csv("../data/meson_semilep/BKinv.csv")
df_BKinv.cl.replace(0, float('nan'), inplace=True)
df_Kpimumu = pd.read_csv("../data/meson_semilep/Kpimumu.csv")
df_Kpimumu.cl.replace(0, float('nan'), inplace=True)
df_Bsmumu = pd.read_csv("../data/meson_semilep/Bsmumu.csv")
df_Bsmumu.cl.replace(0, float('nan'), inplace=True)
df_KLmumu = pd.read_csv("../data/meson_semilep/KLmumu.csv")
df_KLmumu.cl.replace(0, float('nan'), inplace=True)

df_Kpiinv_tau = pd.read_csv("../data/meson_semilep/Kpiinv_tau.csv")
df_Kpiinv_tau.cl.replace(0, float('nan'), inplace=True)
df_BKinv_tau = pd.read_csv("../data/meson_semilep/BKinv_tau.csv")
df_BKinv_tau.cl.replace(0, float('nan'), inplace=True)
df_Bstautau = pd.read_csv("../data/meson_semilep/Bstautau.csv")
df_Bstautau.cl.replace(0, float('nan'), inplace=True)
df_BKtautau = pd.read_csv("../data/meson_semilep/BKtautau.csv")
df_BKtautau.cl.replace(0, float('nan'), inplace=True)

Kpiinv = plots.PlotData(
    r'$K\to \pi +$ inv',
    'goldenrod',
    (0.02, 0.2),
    True,
    df_Kpiinv['ma_GeV'],
    df_Kpiinv['cl'],
    None
)

BKmumu = plots.PlotData(
    r'$B\to K\mu^+\mu^-$',
    'yellowgreen',
    (2.7, 1),
    True,
    df_BKmumu['ma_GeV'],
    df_BKmumu['cl'],
    None
)

BKinv = plots.PlotData(
    r'$B\to K +$ inv',
    'steelblue',
    (0.035, 9.8),
    True,
    df_BKinv['ma_GeV'],
    df_BKinv['cl'],
    None
)

Kpimumu = plots.PlotData(
    r'$K\to \pi \mu^+ \mu^-$',
    'brown',
    (0.16, 1.05),
    True,
    df_Kpimumu['ma_GeV'],
    df_Kpimumu['cl'],
    None
)

Kpiinv_tau = plots.PlotData(
    r'$K\to \pi +$ inv',
    'goldenrod',
    (0.02, 0.7),
    True,
    df_Kpiinv_tau['ma_GeV'],
    df_Kpiinv_tau['cl'],
    None
)

Bsmumu = plots.PlotData(
    r'$B_s \to \mu^+ \mu^-$',
    'lightsalmon',
    (12, 0.1),
    True,
    df_Bsmumu['ma_GeV'],
    df_Bsmumu['cl'],
    None
)

KLmumu = plots.PlotData(
    r'$K_L \to \mu^+ \mu^-$',
    'purple',
    (0.12, 0.23),
    True,
    df_KLmumu['ma_GeV'],
    df_KLmumu['cl'],
    None
)

BKinv_tau = plots.PlotData(
    r'$B\to K +$ inv',
    'yellowgreen',
    (1.6e-3, 27),
    True,
    df_BKinv_tau['ma_GeV'],
    df_BKinv_tau['cl'],
    None
)

Bstautau = plots.PlotData(
    r'$B_s \to \tau^+ \tau^-$',
    'lightsalmon',
    (6, 10),
    True,
    df_Bstautau['ma_GeV'],
    df_Bstautau['cl'],
    None
)

BKtautau = plots.PlotData(
    r'$B\to K\tau^+\tau^-$',
    'yellowgreen',
    (1.25, 400),
    True,
    df_BKtautau['ma_GeV'],
    df_BKtautau['cl'],
    None
)

if __name__ == '__main__':
    BKmumu.textpos = (0.7, 7e-2)
    BKinv_tau.color = 'steelblue'
    plots.make_plot([Kpiinv, BKmumu, BKinv, Kpimumu, Bsmumu, KLmumu], "meson_semilept_lfu.pdf", r'\ell', limx=[1e-3, 10], limy=[1e-2, 2000])
    plots.make_plot([Kpiinv_tau, BKtautau, BKinv_tau, Bstautau], "meson_semilept_tau.pdf", r'\tau', limx=[1e-3, 10], limy=[1e-2, 2000])