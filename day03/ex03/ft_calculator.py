class calculator:
    def __init__(self, other):
        self.other = other

    def __add__(self, object)-> None:
        if isinstance(object, (int, float)):
            result = [item + object for item in self.other]
            self.other  = result
            print(result)
            return calculator(result)
        raise TypeError("Unsupported type")


    def __mul__(self, object) -> None:
        if isinstance(object, (int, float)):
            result = [item * object for item in self.other]
            self.other  = result
            print(result)
            return result

        raise TypeError("Unsupported type")


    def __sub__(self, object) -> None:
        if isinstance(object, (int, float)):
            result = [item - object for item in self.other]
            self.other  = result
            print(result)
            return result

        raise TypeError("Unsupported type")
    # #your code here
    def __truediv__(self, object) -> None:
        if isinstance(object, (int, float)) and object != 0:
            result = [item / object for item in self.other]
            self.other  = result
            print(result)
            return result

        raise TypeError("Unsupported type")
