import matplotlib.pyplot as plt 
from load_csv import load
import sys

from matplotlib.ticker import EngFormatter
def main():
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

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(130)