import numpy as np
def slice_me(family: list, start: int, end: int) -> list:

    family_array = np.array(family)
    print(f"My shape is : {np.shape(family_array)}")
    sclice_array = family_array[start:end]
    print(f"My new shape is : {np.shape(sclice_array)}")

    return sclice_array.tolist()



family = [[1.80, 78.4],
[2.15, 102.7],
[2.10, 98.5],
[1.88, 75.2]]
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))
