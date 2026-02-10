class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        result = sum(a * b for a, b in zip(V1, V2))
        print(f"Dot product is: {result}")
        return result

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        result = [a + b for a, b in zip(V1, V2)]
        print(f"Add Vector is : {[f'{val:.1f}' for val in result]}")
        return result

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        result = [a - b for a, b in zip(V1, V2)]
        print(f"Sous Vector is: {[f'{val:.1f}' for val in result]}")
        return result
