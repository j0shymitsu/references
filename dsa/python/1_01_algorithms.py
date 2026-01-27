def find_minimum(nums):
    min = float("inf")

    if nums == []:
        return None
    
    for num in nums:
        if num < min:
            min = num

    return min

def summed(nums):
    total = 0

    if nums == []:
        return total
    else:
        for num in nums:
            total += num

    return total