
# def generators(lst: range):
#     for i in lst:
#         yield(i)
import os




def ft_tqdm(lst: range):
    # print(next(range))
    try:
        width = os.get_terminal_size().columns
    except OSError:
        width = 80
    total = len(lst)
    bar_len = width - len(f"100%|[]| {total}/{total}") - 1

    for i in lst:
        percent = int((i + 1) / total * 100)
        filled_len = int(bar_len * (i + 1) / total)

        bar = '=' * (filled_len - 1) + '>' + ' ' * (bar_len - filled_len)

        print(f"\r{percent}%|[{bar}]| {i + 1}/{total}", end="", flush=True)
        yield i
    print()

from tqdm import tqdm
from time import sleep
# for elem in tqdm(range(100)):
#     sleep(0.1)
for elem in ft_tqdm(range(100)):
    sleep(0.16)

# def square_numbers(nums):
#     for i in nums:
#         yield(i * i)
# my_num = square_numbers([1,4,2,5])
# for i in my_num:
#     print(i,end='\r')
# print(next(my_num))
