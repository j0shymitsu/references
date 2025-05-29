# Class Variables vs Instance Variables in Python

## Summary

In Python, class variables and instance variables serve different purposes.

Instance variables are unique to each object created from a class and are declared within the constructor method `__init__()`. They can be modified independently for each object, allowing for object-specific data.

Class variables are defined at the class level and are shared among all instances of a class. Changes to a class variable affect all instances, as they reference the same memory location. In other languages, class variables are often referred to as static variables. Class variables should generally be avoided when individual object state differences are needed because they act like global variables, which can complicate program logic.

## Docs

[Python Classes and Instances - Official Python documentation on classes.](https://docs.python.org/3/tutorial/classes.html#a-first-look-at-classes)\
[Static Variables - Wikipedia entry explaining static variables.](https://en.wikipedia.org/wiki/Static_variable)

## Examples

### Instance Variables:
```python
class Spaceship:
    def __init__(self, name):
        self.name = name

enterprise = Spaceship("Enterprise")
millennium_falcon = Spaceship("Millennium Falcon")

enterprise.name = "USS Enterprise"
print(enterprise.name)         # USS Enterprise
print(millennium_falcon.name)  # Millennium Falcon
```
### Class Variables:
```python
class Spaceship:
    crew_capacity = 5

voyager = Spaceship()
galactica = Spaceship()

Spaceship.crew_capacity = 10

print(voyager.crew_capacity)   # 10
print(galactica.crew_capacity) # 10
```