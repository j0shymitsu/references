# Multiple Inheritance Children in Python

## Summary

In object-oriented programming, a parent class can have multiple child classes, forming a tree-like inheritance hierarchy. Each child class can inherit attributes and methods from the parent class, and can also define its own unique attributes and methods. This supports code reuse and logical organization by allowing shared behavior to be defined in a parent class and specialized behavior to be defined in child classes.

## Docs

[Inheritance - Python official documentation](https://docs.python.org/3/tutorial/classes.html#inheritance)

## Examples

### Defining a parent class Hero and multiple child classes:
```python
class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

class Warrior(Hero):
    def __init__(self, name, health, strength):
        super().__init__(name, health)
        self.strength = strength

class Archer(Hero):
    def __init__(self, name, health, arrows):
        super().__init__(name, health)
        self._arrows = arrows

    def shoot(self, target):
        if self._arrows <= 0:
            raise Exception("Not enough arrows")
        self._arrows -= 1
        target.health -= 10
```