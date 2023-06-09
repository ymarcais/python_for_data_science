# x
def square(x: int | float) -> int | float:
    return x * x

# x powered by x
def pow(x: int | float) -> int | float:
    return x ** x

# the count variable retains its value between function calls because 
# it is defined as nonlocal in an outer scope and captured 
# as a closure variable
def outer(x: int | float, function) -> object:
    count = 0
    def inner() -> float:
        nonlocal count
        if count == 0:
            count = x
        count = function(count)
        return count
    return inner

