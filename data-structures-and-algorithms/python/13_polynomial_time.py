# REDUCTION TO P (POLYNOMIAL TIME)

# Non-polynomial
def fib_x(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

# Polynomial runtime
def fib_y(n):
    if n <= 1:
        return n
        
    grandparent = 0
    parent = 1
    
    for i in range(2, n + 1):
        current = parent + grandparent
        grandparent = parent
        parent = current

    return parent
