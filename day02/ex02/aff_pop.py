import matplotlib.pyplot as plt
import numpy as np
from load_csv import load
import sys

def convert_units(series):
    """
    Converts population strings with 'k' or 'M' suffixes to float values.
    """
    def parse_value(val):
        if isinstance(val, str):
            val = val.lower()
            if 'k' in val:
                return float(val.replace('k', '')) * 1e3
            elif 'm' in val:
                return float(val.replace('m', '')) * 1e6
            elif 'b' in val:
                return float(val.replace('b', '')) * 1e9
        return float(val)
    
    return series.apply(parse_value)

def main():
    """
    Extracts years from columns, filters 1800-2050, 
    and plots population comparison.
    """
    df = load('population_total.csv')
    if df is None:
        return

    years_from_file = [col for col in df.columns if col.isdigit() and 1800 <= int(col) <= 2050]
    
    df = df.set_index("country")
    
    country_1 = 'Morocco'
    country_2 = 'Palestine'
    
    try:
        data_1 = convert_units(df.loc[country_1, years_from_file])
        data_2 = convert_units(df.loc[country_2, years_from_file])
    except KeyError as e:
        print(f"Error: Country or Year not found: {e}")
        return

    x_axis = [int(year) for year in years_from_file]
    
    plt.plot(x_axis, data_1, label=country_1)
    plt.plot(x_axis, data_2, label=country_2)

    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend(loc="lower right")

    plt.xticks(np.arange(min(x_axis), max(x_axis) + 1, 40))
    
    plt.yticks([20e6, 40e6, 60e6])
    def format_y(value, tick_number):
        return f'{int(value / 1_000_000)}M'

    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(format_y))
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(130)