# print(filter.__doc__)

def ft_filter(function_to_apply: any, iterable: any):
    new_iterable = [
        item for item in iterable 
        if (function_to_apply(item) if function_to_apply else item)
        ]
    return new_iterable


