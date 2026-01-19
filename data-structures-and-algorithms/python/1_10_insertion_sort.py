# INSERTION SORT
## O(n^2) but tends to be faster than a merge sort on small datasets

def insertion_sort(nums):
    for i in range(1, len(nums)):
        j = i
        while (j > 0) and (nums[j-1] > nums[j]):
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
    return nums