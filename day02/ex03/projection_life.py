import matplotlib.pyplot as plt
from load_csv import load

def parse_value(val):
    """
    Converts strings like '1.2k' to 1200.0 and handles numeric types.
    """
    if isinstance(val, str):
        val = val.lower()
        if 'k' in val:
            return float(val.replace('k', '')) * 1e3
        if 'm' in val:
            return float(val.replace('m', '')) * 1e6
        return float(val)
    return float(val)


def main():
    """
    Loads GDP and Life Expectancy data, filters for the year 1900,
    and displays a scatter plot with a logarithmic scale.
    """
    df_income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    df_life = load("life_expectancy_years.csv")


    if df_income is None or df_life is None:
        return 

    year = "1900"
    income_1900 = df_income[['country',year]].set_index('country')
    life_1900 = df_life[['country', year]].set_index('country')

    data = income_1900.join(life_1900,lsuffix='_income', rsuffix='_life')

    x = data[year + '_income'].apply(parse_value)
    y = data[year + '_life']
    print(x,y)
    plt.scatter(x, y)
    plt.title(year)
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.show()



if __name__ == '__main__':
    main()