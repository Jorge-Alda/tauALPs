import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True
from typing import Sequence, Iterable
from dataclasses import dataclass
from numpy import log10

@dataclass
class PlotData:
    name: str
    color: str|tuple[int, int, int]
    textpos:tuple[int, int]
    solid: bool
    ma: Sequence[float]
    inf: Sequence[float]
    sup: Sequence[float] | None

    def plot(self):
        if self.solid:
            plt.plot(self.ma, self.inf, lw=2.5, c=self.color)
            if self.sup is not None:
                plt.plot(self.ma, self.sup, lw=2.5, c=self.color)
                plt.fill_between(self.ma, self.inf, self.sup, color=self.color, alpha=0.2)
        else:
            plt.plot(self.ma, self.inf, ls = 'dahsed', c=self.color)
            if self.sup is not None:
                plt.plot(self.ma, self.sup, ls='dashed', c=self.color)
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
              limx: tuple[float] = (1e-3, 20),
              limy: tuple[float] = (5e-2, 1e5)
             ):
    fig = plt.figure(figsize=(8, 6))
    for pl in plots:
        if pl.sup is None:
            pl.sup = [1.02*limy[1]]*len(pl.ma)
        pl.plot()
    ax = plt.gca()
    ax.set_xscale('log')
    ax.set_yscale('log')
    plt.xlim(limx)
    plt.ylim(limy)
    plt.xlabel(r'$m_a$ [GeV]', fontsize=18)
    plt.ylabel(r'$|c_{' + lep + '}|/f_a$ [TeV$^{-1}$]', fontsize=18)
    plt.xticks([10**x for x in range(int(log10(limx[0])), 1+int(log10(limx[1])))], labels=erange(int(log10(limx[0])), 1+int(log10(limx[1]))), fontsize=16)
    plt.yticks([10**x for x in range(int(log10(limy[0])), 1+int(log10(limy[1])))], labels=erange(int(log10(limy[0])), 1+int(log10(limy[1]))),fontsize=16)
    if title is not None:
        plt.title(title, fontsize=16)
    plt.tight_layout(pad=0.5)
    plt.savefig(filepath)