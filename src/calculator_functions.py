def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError()
    return a * b

def divide(a, b):
    return a / b

def new_divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

