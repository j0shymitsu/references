# Classes in Python

## Summary

In Python, a class is a blueprint for creating objects. It defines a new data type, encapsulating attributes and behaviors. Attributes are variables inside the class, and behaviors are defined by methods. Classes allow for the creation of custom types, enabling an organized approach to modeling real-world concepts within code.

An object is an instance of a class. When you create an object, you are instantiating a class, which allocates memory to store the object's attributes and permits access to its methods.

## Docs

[Python Classes and Instances](https://docs.python.org/3/tutorial/classes.html)

## Examples

### Defining a class and creating instances:
```python
class Wizard:
    mana = 100
    spells = 5

# Create instances of the Wizard class
gandalf = Wizard()
merlin = Wizard()

# Access class attributes
print(gandalf.mana)  # 100
print(merlin.spells) # 5
```
### Creating a class with different attributes:
```python
class Tower:
    height = 20
    defense = 15

# Create an instance of the Tower class
watchtower = Tower()

# Access class attributes
print(watchtower.height)  # 20
print(watchtower.defense) # 15
```