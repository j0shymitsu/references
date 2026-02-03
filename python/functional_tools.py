from functools import reduce
from functools import lru_cache

# lambda functions
def file_type_getter(file_extension_tuples):

    extension_list = {}

    for file, spec in file_extension_tuples:
        for file_type in spec:
            extension_list[file_type] = file
    
    get_file_type = lambda file_type: extension_list.get(file_type, "Unknown")
    
    return get_file_type

file_extension_tuples = [
    ("document", [".doc", ".docx", ".pdf", ".txt"]),
    ("image", [".jpg", ".jpeg", ".png", ".gif", ".bmp"]),
    ("audio", [".mp3", ".wav", ".flac"]),
    ("video", [".mp4", ".avi", ".mov", ".mkv"]),
    ("archive", [".zip", ".rar", ".7z", ".tar.gz"]),
    ("code", [".py", ".js", ".java", ".c", ".cpp"]),
    ("spreadsheet", [".xls", ".xlsx", ".csv"]),
    ("presentation", [".ppt", ".pptx"]),
]

get_file_type = file_type_getter(file_extension_tuples)

print(get_file_type(".docx"))
print(get_file_type(".png"))
print(get_file_type(".mp3"))
print(get_file_type(".unknown"))

######
print("\n")

numbers = [1, 2, 3, 4, 5, 6]
a = [1, 2, 3]
b = [4, 5, 6]

# map: apply a function to each item in an iterable
tripled = map(lambda x: x * 3, numbers)
print(list(tripled))    # expected output: [3, 6, 9, 12, etc]

# filter: filter items in an iterable by condition
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))      # expected output: [2, 4, 6, etc]

# reduce: reduce an iterable to a single value
product = reduce(lambda x, y: x * y, numbers)
print(product)

product_init = reduce(lambda x, y: x * y, numbers, 10)  # with initialiser; start with 10 instead of first element
print(product_init)

# zip: take two iterables and return new iterable where each element is a tuple containing one element from each
c = list(zip(a, b))
print(c)

# more lambda
def sort_dates(dates):
    dates_copy = dates.copy()
    
    sorted_dates = sorted(dates_copy, key=lambda date: (date.split('-')[2], date.split('-')[0], date.split('-')[1]))
    return sorted_dates

#lru_cache
@lru_cache()
def is_palindrome(word):
    if len(word) <= 1:
        return True
    elif word[0] != word[-1]:
        return False
    new_word = word[1:-1]
    return is_palindrome(new_word)
