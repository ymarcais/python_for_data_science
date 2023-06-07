class Calculator:
    def __init__(self, vector):
        self.vector = vector
                    
    def __add__(self, scalar):
        result = [element + scalar for element in self.vector]
        self.vector = result
        return self.vector
    
    def __mul__(self, scalar):
        result = [element * scalar for element in self.vector]
        self.vector = result
        return self.vector
    
    def __sub__(self, scalar):
        result = [element - scalar for element in self.vector]
        self.vector = result
        return self.vector
    
    def __truediv__(self, scalar):
        if scalar != 0:
            result = [element / scalar for element in self.vector]
        else:
            result = "Error Dividing By 0 Undefined"
        return result
    
    def check_decorator(func):
        def wrapper(V1, V2):
            if len(V1) != len(V2):
                print("Error: Vectors must have identical sizes.")
                exit()
            return func(V1, V2)     
        return wrapper
    
    @staticmethod
    @check_decorator
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        result = sum(v1 * v2 for v1, v2 in zip(V1, V2))
        print("Dot product is:", result)
        return result
    
    @staticmethod
    @check_decorator
    def add_vec(V1: list[float], V2: list[float]) -> None:
        result = [float(v1) + float(v2) for v1, v2 in zip(V1, V2)]
        print("Add Vector is:", result)

    @staticmethod
    @check_decorator
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        result = [float(v1) - float(v2) for v1, v2 in zip(V1, V2)]
        print("Sous Vector is:", result)
