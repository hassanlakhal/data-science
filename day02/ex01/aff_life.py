import matplotlib.pyplot as plt 
from load_csv import load

from matplotlib.ticker import EngFormatter

df = load("life_expectancy_years.csv")


df = df.set_index("country")
morocco = df.loc['Morocco']
x = morocco.index 
y = morocco.values

plt.figure(figsize=(5, 5))

plt.plot(x,y)
plt.xlabel("Year")
plt.xticks(morocco.index[::40])
plt.ylabel("Life expectancy")
plt.title("Morocco Life expectancy Projections")

plt.show()
