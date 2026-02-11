from typing import Any

def ft_mean(*args: Any):
    if len(args) == 0:
        return
    total = sum(args)
    return (total / len(args))

def ft_median(*args: Any):
    if len(args) == 0:
        return
    sortedLst = sorted(args)
    lstLen = len(args)
    index = (lstLen - 1) // 2
    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1]/2.0)

def ft_quartile(*args: Any):
    if len(args) == 0:
        return
    ortedLst = sorted(args)
    n = len(ortedLst)
    if n % 2 == 0:
        lower_half = ortedLst[:n//2]
        upper_half = ortedLst[n//2:]
    else:
        lower_half = ortedLst[:n//2 + 1]
        upper_half = ortedLst[n//2:]

    Q1 = float(ft_median(*lower_half))
    Q2 = float(ft_median(*upper_half))

    return [Q1, Q2]

def ft_variance(*args: Any):
    if len(args) == 0:
        return
    mean = ft_mean(*args)
    return sum((x - mean)**2 for x in args) / len(args)

def ft_std(*args: Any):
    var = ft_variance(*args)
    return var ** 0.5


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    for stat in kwargs.values():
        if stat == 'mean':
            result = ft_mean(*args)
            print("mean :" + f'{result}' if result is not None else 'ERROR')
        elif stat == 'median':
            result = ft_median(*args)
            print("median :" + f'{result}' if result is not None else 'ERROR')
        elif stat == 'quartile':
            result = ft_quartile(*args)
            print("quartile :" + f'{result}' if result is not None else 'ERROR')
        elif stat == 'std':
            result = ft_std(*args)
            print("std :" + f'{result}' if result is not None else 'ERROR')
        elif stat == 'var':
            result = ft_variance(*args)
            print("var :" + f'{result}' if result is not None else 'ERROR')