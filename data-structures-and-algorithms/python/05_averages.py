import math

# CALCULATING MEAN
def average_followers(nums):
    if not nums:
        return None
    else:
        return sum(nums) / len(nums)
    
# CALCULATING MEDIAN
## Calculating the median is typically more applicable in CS if data can be
## sorted
def median_followers(nums):
    if not nums:
        return None
    else:
        # Even numbered lists
        if len(nums) % 2 == 0:
            index_a = math.floor(len(nums)) / 2
            index_b = index_a - 1
            return (nums[int(index_a)] + nums[int(index_b)]) / 2
        # Odd numbered lists
        return nums[int(len(nums) / 2)]

print(median_followers([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 22, 60]))