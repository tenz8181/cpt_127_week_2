# 1. Function to add two numbers
def add_two_numbers(2, 3):
    return 2 + 3

# 2. Function to multiply with an optional multiplier
def multiplier(number, multiplier=2):
    return number * multiplier

# 3. Function to divide two numbers and return quotient and remainder
def divider(dividend, divisor):
    if divisor == 0:
        raise ValueError("The divisor cannot be zero.")
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder
