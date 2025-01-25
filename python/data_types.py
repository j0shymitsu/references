x = 4
pi = 3.141
y = "Wecome"
password_correct = True

# Python works without having to declare the data type.

username = input("Please enter your username > ")
print(f"\nUsername is: {username}" "\n")
print(y)
print("\nPi is", pi)
print("\nThe secret number is", x)

###

x = 12
pi = 3.14159265
message = "Hello world"
password_correct = True

print("x is a", type(x))
print("Pi is a", type(pi))
print("Message is a", type(message))
print("Password correct check is", type(password_correct))

if type(x) == int:
    x = 2*x
    print("x * 2 =", x)

if type(message) == str:
    message = message + ", let's learn Python"
    print(message)