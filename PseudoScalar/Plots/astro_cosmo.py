import plots
import pandas as pd
import particle.literals

me = particle.literals.e_minus.mass / 1e6 # TeV

df_sn1987a = pd.read_csv('../data/astro_cosmo/SN1987.csv')

sn1987a = plots.PlotData(
    'SN 1987A',
    'k',
    (2e-3, 1e-2),
    True,
    df_sn1987a['ma_GeV'],
    df_sn1987a['gae_inf']/me,
    df_sn1987a['gae_sup']/me
)

if __name__ == '__main__':
    plots.make_plot([sn1987a], 'astro_cosmo.pdf', r'\ell')