### SIMPLE FIND EXAMPLE ###

message = "Happy New Year"
x = message.find(" ")
print(message.find(" ", x+1))

message_list = message.split()
print(message_list)

for y in message_list:
    print(y[0], end="")
print()

name = "Josh Birch"

name_list = name.split()
print(name_list)

for y in name_list:
    print(y[0], end="")
print()

newMessage = message.replace("New Year", "Birthday")
print(newMessage)

