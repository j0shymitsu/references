# Recursive function for factorial
def factorial(n):
    # Base case: factorial(0) is 1
    if n == 0:
        return 1
    else:
        # Recursive case: n! = n * (n-1)!
        return n * factorial(n-1)


# Function to find the maximum depth of dictionary nesting
def dict_depth(d, max_depth_so_far):
    # If it's not a dictionary or it's empty, return the current depth
    if not isinstance(d, dict) or not d:
        return max_depth_so_far
    
    current_max = max_depth_so_far

    # Explore each value in the dictionary
    for v in d.values():
        # Recursively calculate depth of nested dicts
        depth_of_subdict = dict_depth(v, max_depth_so_far + 1)

        # Update current_max if we find a deeper level
        if depth_of_subdict > current_max:
            current_max = depth_of_subdict

    return current_max


# Function to print each character in a word using recursion
def print_chars(word, i):
    # Base case: stop when index reaches length of word
    if i == len(word):
        return
    # Print the current character
    print(word[i])
    # Recurse with the next index
    print_chars(word, i + 1)

# Example usage: prints each character of "Hello" on a new line
print_chars("Hello", 0)


# Function that builds a dictionary by "zipping" two lists
def zipmap(keys, values):
    # Base case: stop when either list runs out
    if not keys or not values:
        return {}
    # Recursive step: build dictionary for the rest of the list
    result = zipmap(keys[1:], values[1:])
    # Add the current key-value pair
    result[keys[0]] = values[0]

    return result


# Recursive countdown function
def countdown(n):
    # Print the current number
    print(n)
    # Base case: stop when n reaches 0
    if n == 0:
        return
    else:
        # Recursive step: decrement n
        countdown(n - 1)


# Function to calculate sum of a nested list
def sum_nested_list(lst):
    total_size = 0
    
    for item in lst:
        # If item is an integer, add it directly
        if isinstance(item, int):
            total_size += item
        # If item is a list, recurse into it
        if isinstance(item, list):
            total_size += sum_nested_list(item)

    return total_size


# Recursively list all files from a nested directory structure
# Example structure:
# { "folder": {"file.txt": None, "subfolder": {"nested.txt": None}} }
def list_files(parent_directory, current_filepath=""):
    file_paths = []
    
    for key in parent_directory:
        # Build the new file path by appending the current key
        new_file_path = current_filepath + "/" + key
        if parent_directory[key] is None:
            # If the value is None, it's a file
            file_paths.append(new_file_path)
        else:
            # Otherwise, recurse into the subdirectory
            file_paths.extend(list_files(parent_directory[key], new_file_path))

    return file_paths


# Function to find how deep a target document is nested in a dict
def count_nested_levels(nested_documents, target_document_id, level=1):
    for document_id, nested in nested_documents.items():
        # If we find the target, return its level
        if document_id == target_document_id:
            return level

        # If the value is another dict, recurse into it
        if isinstance(nested, dict):
            nested_level = count_nested_levels(nested, target_document_id, level + 1)

            # If target was found deeper inside, return that level
            if nested_level != -1:
                return nested_level

    # Return -1 if target not found at this branch
    return -1
