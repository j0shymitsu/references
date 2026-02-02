# FACTORIALS
def factorial(n):
    # Assuming n is a non-negative integer
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product
