def count_in_list(lst: list, word: str) -> int:
    count = 0
    for elem in lst:
        if elem == word:
            count = count + 1
    return count