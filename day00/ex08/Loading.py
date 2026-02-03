
import os


def ft_tqdm(lst: range):
    try:
        width = os.get_terminal_size().columns
    except OSError:
        width = 80
    total = len(lst)
    bar_len = width - len(f"100%|[]| {total}/{total}") - 1

    for i in lst:
        percent = round((i + 1) / total * 100)
        filled_len = int(bar_len * (i + 1) / total)

        bar = '=' * (filled_len - 1) + '>' + ' ' * (bar_len - filled_len)

        print(f"\r{percent}%|[{bar}]| {i + 1}/{total}", end="", flush=True)
        yield i
    print()

from tqdm import tqdm
from time import sleep
# for elem in tqdm(range(333)):
#     sleep(0.9)
for elem in ft_tqdm(range(333)):
    sleep(0.9)
