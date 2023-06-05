class Calculator:
    def __init__(self, vector):
        self.vector = vector
    
    def __add__(self, scalar):
        result = [element + scalar for element in self.vector]
        return result
    
    def __mul__(self, scalar):
        result = [element * scalar for element in self.vector]
        return result
    
    def __sub__(self, scalar):
        result = [element - scalar for element in self.vector]
        return result
    
    def __truediv__(self, scalar):
        result = [element / scalar for element in self.vector]
        return result
