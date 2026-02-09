from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def main():
    df_1 = load('income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
    df_2 = load('life_expectancy_years.csv')


    df_1 = df_1.set_index("country")
    df_2 = df_2.set_index("country")

    data_1 = df_1["1900"]
    data_2 = df_2["1900"]
    # frames = [data_1.values, data_2.values]

    # result = pd.concat(frames)

    data_2 = np.nan_to_num(data_2 , nan=0)
    print(data_1.values)
    print("-------------------------")
    print(data_2)
    # print(result.shape)
    plt.scatter(data_2, data_1)
    plt.show()



if __name__ == '__main__':
    main()