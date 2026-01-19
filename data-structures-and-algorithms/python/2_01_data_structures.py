# DATA STRUCTURES
    ## A data structure is a data organisation, management, and storage format that enables
    ## efficient access and modification. More precisely, a data structure is a collection of data values,
    ## the relationship among them, and teh functions or operations that can be applied to
    ## the data.

# PYTHONS BUILT IN DATA STRUCTURES
## List
    ## Lists are good for: Appending (O(1)), accessing by index (typically O(1)),
    ## deleting (O(n)) and searching (O(n)). They start to struggle if you need to
    ## frequently delete items from the middle of the list, or frequently search the
    ## entire list.
def count_marketers(job_titles):
    count = 0
    for item in job_titles:
        item = item.lower()
        if "marketer" in item:
            count += 1
    return count

def last_work_experience(work_experiences):
    if work_experiences == []:
        return None
    else:
        return work_experiences[-1]

## Dictionary
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}