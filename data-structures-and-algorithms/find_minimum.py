def find_minimum(nums):
    min = float("inf")

    if nums == []:
        return None
    
    for num in nums:
        if num < min:
            min = num

    return min