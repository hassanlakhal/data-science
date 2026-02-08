from load_csv import load
import matplotlib.pyplot as plt
from pandas import Series
from matplotlib.ticker import MultipleLocator, FuncFormatter
import numpy as np 

import sys


def convert_units(series: Series):
    s = series.str.strip()

    s = s.str.replace("k","e3",regex=False)
    s = s.str.replace("M","e6",regex=False)
    
    return s.astype(float)

df = load('population_total.csv')
df = df.set_index("country")
morocco = df.loc['France']
palestine = df.loc['Belgium']

x = morocco.index.astype(int)

ym = convert_units(morocco)
yp = convert_units(palestine)

plt.plot(x,ym)
plt.plot(x,yp)

start , end = plt.ylim(min(ym.min(), yp.min()), max(ym.max(), yp.max()))
plt.yticks(np.arange(start , end, 20e6))


plt.gca().yaxis.set_major_formatter(
    FuncFormatter(lambda y, _: f'{y/1_000_000:.1f}M')
)
plt.xlim(min(x), max(x))

plt.xticks(np.arange(min(x), max(x)+1, 40))
plt.show()
# print(palestine)


