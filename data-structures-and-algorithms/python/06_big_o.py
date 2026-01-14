# BIG O NOTATION

# O(n) EXAMPLE
def find_max(nums):
    largest = float('-inf')
    for item in nums:
        if item > largest:
            largest = item
    return largest

# O(n^2) EXAMPLE
## Grow in complexity much more rapidly but can work for small-medium input
def does_name_exist(first_names, last_names, full_name):
    for forename in first_names:
        for surname in last_names:
            if(f'{forename} {surname}') == full_name:
                return True
    return False

# O(nm) EXAMPLE
## Very similar to O(n^2), but instead of a single input, there are two
## If n & m increase at the same rate, effectively the same as O(n^2), but if
## one increases faster or slower, the it's useful to track their complexity
## separately
def get_avg_brand_followers(all_handles, brand_name):
    count = 0
    for lists in all_handles:
        for handle in lists:
            if brand_name in handle:
                count += 1
    return count / len(all_handles)