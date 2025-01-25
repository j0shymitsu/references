### BITWISE AND

# Equals 5; checks if true (1) in both positions and returns resulting binary num
print(0b0101 & 0b0111)

can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001

def get_create_bits(user_permissions):
    user_create_guild_permission = user_permissions & can_create_guild
    return user_create_guild_permission


def get_review_bits(user_permissions):
    user_review_guild_permission = user_permissions & can_review_guild
    return user_review_guild_permission


def get_delete_bits(user_permissions):
    user_delete_guild_permission = user_permissions & can_delete_guild
    return user_delete_guild_permission


def get_edit_bits(user_permissions):
    user_edit_guild_permission = user_permissions & can_edit_guild
    return user_edit_guild_permission


### BITWISE OR

a = 0b0101  # 5
b = 0b0011  # 3

# Perform bitwise OR
result = a | b

print(f"a = {a} (Binary: {bin(a)})")
print(f"b = {b} (Binary: {bin(b)})")
print(f"Result of a | b: {result} (Binary: {bin(result)})")
