# Encapsulation in Python

## Summary

Encapsulation is a fundamental concept in object-oriented programming that involves hiding the internal state and functionality of an object and only exposing a controlled interface. This helps manage complexity by allowing the user to interact with the object through a simple interface while the internal workings remain hidden.

In Python, encapsulation is achieved through public and private members of a class. By default, attributes and methods in a class are public. To make a member private, it's prefixed with double underscores (__). This restricts direct access from outside the class, encouraging interaction through public methods.

## Docs

[Python Classes](https://docs.python.org/3/tutorial/classes.html)\
[Encapsulation](https://en.wikipedia.org/wiki/Encapsulation_(computer_programming))

## Examples

### Defining a class with public and private members:
```python
class Character:
    def __init__(self, health, stamina):
        self.__armor = health  # Private attribute
        self.__stamina = stamina  # Private attribute

    def get_health(self):
        return self.__armor

hero = Character(100, 50)
print(hero.get_health())  # Accessing via public method
# 100
```
### Attempting to access a private attribute directly results in an error:
```python
class Fortress:
    def __init__(self, walls, guards):
        self.__walls = walls
        self.__guards = guards

    def get_security(self):
        return self.__walls + self.__guards

bastion = Fortress(5, 20)

# This will raise an AttributeError
print(bastion.__walls)

# Correct way to access the information
print(bastion.get_security())
# 25
```