#!/usr/bin/python3
if __name__ == "__main__":
    """Print the sum, difference, multiple and quotient of 10 and 5."""
from calculator_1 import add, sub, mul, div
a = 10
b = 5
returns_of_add = add(a, b)
returns_of_sub = sub(a, b)
returns_of_mul = mul(a, b)
returns_of_div = div(a, b)
print("{} + {} = {}".format(a, b, returns_of_add))
print("{} - {} = {}".format(a, b, returns_of_sub))
print("{} * {} = {}".format(a, b, returns_of_mul))
print("{} / {} = {}".format(a, b, returns_of_div))
