# Constructors in Python

## Summary

In Python, constructors are methods used to set up an object's properties when a class instance is made. The constructor is defined with the init method, where attributes are usually set. Constructors can accept parameters for flexible object setup.

## Docs

[Python Data Model: __init__](https://docs.python.org/3/reference/datamodel.html#object.__init__)

## Examples

### Defining a class with a constructor:
```python 
class Wizard:
    def __init__(self, name, power):
        self.name = name
        self.power = power

gandalf = Wizard("Gandalf", "Magic")
print(gandalf.name)   # Gandalf
print(gandalf.power)  # Magic
```
### Using constructor parameters to initialize attributes:
```python
class Fortress:
    def __init__(self, walls, towers):
        self.walls = walls
        self.towers = towers

castle = Fortress(4, 2)
print(castle.walls)   # 4
print(castle.towers)  # 2
```