import math

# Travelling salesman problem
def tsp(cities, paths, dist):
    possible = permutations(cities)
    for path in possible:
        total = 0
        for i in range(len(path) - 1):
            total += paths[path[i]][path[i + 1]]
        if total < dist:
            return True
    return False

def verify_tsp(paths, dist, actual_path):
    sum = 0
    for i in range(1, len(actual_path)):
        sum += paths[actual_path[i-1]][actual_path[i]]
    return sum < dist

def permutations(arr):
    res = []
    res = helper(res, arr, len(arr))
    return res


def helper(res, arr, n):
    if n == 1:
        tmp = arr.copy()
        res.append(tmp)
    else:
        for i in range(n):
            res = helper(res, arr, n - 1)
            if n % 2 == 1:
                arr[n - 1], arr[i] = arr[i], arr[n - 1]
            else:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]
    return res

###
# Num of guesses
###
def get_num_guesses(length):
    total = 0
    for i in range(length):
        total += 26 ** (i + 1)
    return total

###
### Prime Factors
###
def prime_factors(n):
    prime_factors = []
    while n % 2 == 0:
        n /= 2
        prime_factors.append(2)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % 1 == 0:
            n /= 1
            prime_factors.append(i)
    if n > 2:
        prime_factors.append(int(n))
    return sorted(prime_factors)

###
# Subet sum problem
###