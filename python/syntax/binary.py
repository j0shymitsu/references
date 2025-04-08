num_servers = "101"
num_players = "11010"
num_admins = "1111"

def binary_string_to_int(num_servers, num_players, num_admins):
    num_servers = int(num_servers, 2)
    num_players = int(num_players, 2)
    num_admins = int(num_admins, 2)

    return num_servers, num_players, num_admins

print(binary_string_to_int(num_servers, num_players, num_admins))