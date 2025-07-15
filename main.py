
"""
Demonstrates how to use the functools.reduce function with examples for sum and product.
"""

from functools import reduce

if __name__ == "__main__":

    # Example: Sum of a list of numbers
    numbers = [1, 2, 3, 4, 5]
    total = reduce(lambda x, y: x + y, numbers)
    print(f"Sum of {numbers} is {total}")

    # Example: Product of a list of numbers
    product = reduce(lambda x, y: x * y, numbers)
    print(f"Product of {numbers} is {product}")