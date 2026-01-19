# MERGE SORT
## O(n*log(n)): calls itself recursively
def merge_sort(nums):
    if len(nums) < 2:
        return nums
    else:
        mid = len(nums) // 2
        nums_a = nums[:mid]
        nums_b = nums[mid:]
        sorted_a = merge_sort(nums_a)
        sorted_b = merge_sort(nums_b)
        return merge(sorted_a, sorted_b)
    
def merge(first, second):
    final = []
    i = j = 0
    while (i < len(first)) and (j < len(second)):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
    for x in range(i, len(first)):
        final.append(first[x])
    for y in range(j, len(second)):
        final.append(second[y])
    return final