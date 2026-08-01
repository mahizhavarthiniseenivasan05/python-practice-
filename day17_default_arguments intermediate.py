# Day 17 - Default Arguments

def greet(name="Mahizhavarthini"):
    print("Welcome", name)

# Default value
greet()

# User value
greet("Rahul")


def add(a, b=10):
    print("Sum =", a + b)

# Default argument
add(5)

# Custom argument
add(5, 20)