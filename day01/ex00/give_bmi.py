import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:

    height_array = np.array(height)
    weight_array = np.array(weight)
    bmi = weight_array / ( height_array ** 2)

    bmi_list = bmi.tolist()

    return bmi_list


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    bmi_array = np.array(bmi)
    bmi_limit = bmi_array > limit

    bmi_limit_list = bmi_limit.tolist()

    return bmi_limit_list
height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))




