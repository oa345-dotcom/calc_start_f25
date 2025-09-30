def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
# export public API so "from src import addition" works reliably
__all__ = ["addition", "subtraction", "multiply", "divide"]
