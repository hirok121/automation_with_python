# Calculator code
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

# Testing the calculator functions
print(add(5, 3))        # Output: 8
print(subtract(10, 4))  # Output: 6
print(multiply(2, 6))   # Output: 12
print(divide(10, 2))    # Output: 5
print(divide(10, 0))    # Output: Error: Division by zero is not allowed.
