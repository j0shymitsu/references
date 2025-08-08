numbers = [1, 2, 3, 4, 5, 6]

# map: apply a function to each item in an iterable
tripled = map(lambda x: x * 3, numbers)
print(list(tripled))    # expected output: [3, 6, 9, 12, etc]

# filter: filter items in an iterable by condition
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))      # expected output: [2, 4, 6, etc]

