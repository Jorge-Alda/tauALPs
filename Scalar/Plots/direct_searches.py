import plots
import pandas as pd

fa = 1000
vev = 246

# df_gammainv_inf = pd.read_csv('../data/direct_searches/gammainv_inf.csv')
# df_gammainv_proj = pd.read_csv('../data/direct_searches/gammainv_proj.csv')
# df_ee3gamma = pd.read_csv('../data/direct_searches/ee3gamma.csv')
# df_ee3gamma_proj = pd.read_csv('../data/direct_searches/ee3gamma_proj.csv')
df_eetaugamma = pd.read_csv('../data/direct_searches/eetaugamma.csv')
df_eetaugamma_proj = pd.read_csv('../data/direct_searches/eetaugamma_proj.csv')


# gammainv = plots.PlotData(
#     r'$e^+e^-\to \gamma +$ inv',
#     'slategray',
#     (3e-3, 12),
#     True,
#     df_gammainv_inf['ma_GeV'],
#     df_gammainv_inf['cl_inf'],
#     df_gammainv_inf['cl_sup']
# )

# gammainv_proj = plots.PlotData(
#     r'$e^+e^-\to \gamma +$ inv' + '\n' + r'  (50 ab$^{-1}$)',
#     'slategray',
#     (3e-3, 1.6),
#     False,
#     df_gammainv_proj['ma_GeV'],
#     df_gammainv_proj['cl_inf'],
#     df_gammainv_proj['cl_sup']
# )

# ee3gamma = plots.PlotData(
#     r'$e^+e^-\to 3\gamma$',
#     'teal',
#     (3e-2, 80),
#     True,
#     df_ee3gamma['ma_GeV'],
#     df_ee3gamma['cl'],
#     None
# )

# ee3gamma_proj = plots.PlotData(
#     r'$e^+e^-\to 3\gamma$' +'\n' + r'(50 ab$^{-1}$)',
#     'teal',
#     (13e-2, 2),
#     False,
#     df_ee3gamma_proj['ma_GeV'],
#     df_ee3gamma_proj['cl'],
#     None
# )

eetaugamma = plots.PlotData(
    r'$e^+e^-\to \tau^+\tau^-\gamma\gamma$',
    'red',
    (1, 120),
    True,
    df_eetaugamma['ma_GeV'],
    df_eetaugamma['cl'],
    None
)

eetaugamma_proj = plots.PlotData(
    r'$e^+e^-\to \tau^+\tau^-\gamma\gamma$' + '\n' + r'(50 ab$^{-1}$)',
    'red',
    (1, 0.75),
    False,
    df_eetaugamma_proj['ma_GeV'],
    df_eetaugamma_proj['cl'],
    None
)
