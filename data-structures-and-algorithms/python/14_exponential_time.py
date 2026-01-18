# EXPONENTIAL TIME O(2^N)
## If one subset could be calculated per millisecond, just 25 items here would take 9 hours
def power_set(input):
    if input == []:
        return [[]]
    else:
        all_subsets = [[]]
        for item in input:
            new_subsets = []
            for subset in all_subsets:
                new_subset = subset + [item]
                new_subsets.append(new_subset)
            all_subsets.extend(new_subsets)
    return all_subsets