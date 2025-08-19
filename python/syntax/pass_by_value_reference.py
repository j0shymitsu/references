# When you pass a value into a function as an argument, one of two things can happen:

# - It's passed by reference: The function has access to the original value and can change it.
# - It's passed by value: The function only has access to a copy. Changes to the copy within the function don't affect the original.

# There is a bit more nuance, but this explanation mostly works.

# These types are passed by reference:

#    Lists
#    Dictionaries
#    Sets

#These types are passed by value:

#    Integers
#    Floats
#    Strings
#    Booleans
#    Tuples

# Most collection types are passed by reference (except for tuples) and most primitive types are passed by value.

# PASS BY REFERENCE EXAMPLE (MUTABLE)
def modify_list(inner_lst):
    inner_lst.append(4)
    # the original "outer_lst" is updated
    # because inner_lst is a reference to the original

outer_lst = [1, 2, 3]
modify_list(outer_lst)
# outer_lst = [1, 2, 3, 4]


# PASS BY VALUE EXAMPLE (IMMUTABLEs)
def attempt_to_modify(inner_num):
    inner_num += 1
    # the original "outer_num" is not updated
    # because inner_num is a copy of the original

outer_num = 1
attempt_to_modify(outer_num)
# outer_num = 1
