negative_infinity = float("-inf")
positive_infinity = float("inf")

# Working example
def find_max(nums):
    max_so_far = float("-inf")

    for num in nums:
        if num > max_so_far:
            max_so_far = num

    return max_so_far

print(find_max([1, 2, 300, 4, 5]))