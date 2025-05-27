# Inheritance Hierarchy in Python

## Summary

Inheritance in object-oriented programming allows a class, known as a child class, to inherit attributes and methods from another class, known as a parent class. This creates a hierarchy where the child class can reuse, extend, or modify the behavior defined in the parent class. Inheritance enables code reusability and logical structuring of classes.

When designing inheritance hierarchies, ensure that the child class is a strict subset of its parent class. Avoid unnecessary complexity by preventing excessive nesting of inheritance trees. Child classes do not have direct access to the private properties of their parent classes; they must use provided methods (like getters) to access such properties.

## Docs

[Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)\
[Classes and Objects](https://docs.python.org/3/tutorial/classes.html)

## Examples

### Using Inheritance to Create a Castle from a Wall:
```python
class Wall:
    def __init__(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

class Castle(Wall):
    def __init__(self, height, towers):
        super().__init__(height)
        self.towers = towers

    def get_tower_height(self):
        return self.get_height() * 2

castle = Castle(10, 4)
print(castle.get_tower_height())
# Output: 20
```