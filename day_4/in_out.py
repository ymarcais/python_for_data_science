# x squared
def square(x: int | float) -> int | float:
    return x * x

# x powered by x
def pow(x: int | float) -> int | float:
    return x ** x

# Use an array to store the counter value
def outer(x: int | float, function) -> object:
    counter = [x]  
    def inner(static=counter) -> float:
        static[0] = function(static[0])
        return static[0]
    return inner

