import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True
from typing import Sequence, Iterable
from dataclasses import dataclass
from numpy import log10, pi, sqrt

@dataclass
class PlotData:
    name: str
    color: str|tuple[int, int, int]
    textpos:tuple[int, int]
    solid: bool
    ma: Sequence[float]
    inf: Sequence[float]
    sup: Sequence[float] | None
    legend: bool = False

    def plot(self):
        if self.solid:
            plt.plot(self.ma, self.inf, lw=2.5, c=self.color, label = self.name.replace('\n', ' '))
            if self.sup is not None:
                plt.plot(self.ma, self.sup, lw=2.5, c=self.color)
                plt.fill_between(self.ma, self.inf, self.sup, color=self.color, alpha=0.2)
        else:
            plt.plot(self.ma, self.inf, ls = 'dashed', c=self.color)
            if self.sup is not None:
                plt.plot(self.ma, self.sup, ls='dashed', c=self.color)
        if not self.legend:
            plt.annotate(self.name, self.textpos, fontsize=14, c=self.color)

@dataclass
class PlotDataClosed:
    name: str
    color: str|tuple[int, int, int]
    textpos:tuple[int, int]
    solid: bool
    ma: Sequence[float]
    inf: Sequence[float]
    sup: Sequence[float] | None = None
    legend: bool = False

    def plot(self):
        if self.solid:
            plt.plot(self.ma, self.inf, lw=2.5, c=self.color, label = self.name.replace('\n', ' '))
            plt.fill(self.ma, self.inf, color=self.color, alpha=0.2)
        else:
            plt.plot(self.ma, self.inf, ls = 'dashed', c=self.color)
        if not self.legend:
            plt.annotate(self.name, self.textpos, fontsize=14, c=self.color)

@dataclass
class PlotDataGauge:
    name: str
    color: str|tuple[int, int, int]
    textpos:tuple[int, int]
    ma: Sequence[float]
    nogauge: Sequence[float]
    gaugeplus: Sequence[float]
    gaugeminus: Sequence[float]
    legend: bool = False
    sup = None

    def plot(self):
        plt.plot(self.ma, self.nogauge, lw=2.5, c=self.color, label = self.name.replace('\n', ' '))
        plt.plot(self.ma, self.gaugeplus, lw=1.5, ls='dotted', c=self.color)
        plt.plot(self.ma, self.gaugeminus, lw=1.5, ls='dashed', c=self.color)
        if not self.legend:
            plt.annotate(self.name, self.textpos, fontsize=14, c=self.color)

def erange(start, end):
    for i in range(start, end):
        if i ==0 :
            yield '$1$'
        elif i == 1:
            yield '$10$'
        else:
            yield r'$10^{'+str(i)+'}$'

def make_plot(plots: Iterable[PlotData],
              filepath: str,
              lep: str,
              title: str | None = None,
              limx: tuple[float] = (1e-3, 1000),
              limy: tuple[float] = (5e-2, 1e5),
              legend: bool = False,
              legend_args = {}
             ):
    fig = plt.figure(figsize=(8, 6))
    for pl in plots:
        pl.legend = legend
        if pl.sup is None:
            pl.sup = [1.02*limy[1]]*len(pl.ma)
        pl.plot()
    ax = plt.gca()
    ax.set_xscale('log')
    ax.set_yscale('log')
    plt.xlim(limx)
    plt.ylim(limy)
    plt.xlabel(r'$m_\phi$ [GeV]', fontsize=20)
    plt.ylabel(r'$|y_{' + lep + '}|/f_\phi$ [TeV$^{-1}$]', fontsize=20)
    plt.xticks([10**x for x in range(int(log10(limx[0])), 1+int(log10(limx[1])))], labels=erange(int(log10(limx[0])), 1+int(log10(limx[1]))), fontsize=20)
    plt.yticks([10**x for x in range(int(log10(limy[0])), 1+int(log10(limy[1])))], labels=erange(int(log10(limy[0])), 1+int(log10(limy[1]))),fontsize=20)
    if title is not None:
        plt.title(title, fontsize=20)
    if legend:
        plt.legend(**legend_args)
    plt.fill_between(limx, [sqrt(8*pi/3)*1000/1.77,sqrt(8*pi/3)*1000/1.77], [limy[1], limy[1]], color='none', edgecolor='gray', hatch='/')
    plt.tight_layout(pad=0.5)
    plt.savefig(filepath)