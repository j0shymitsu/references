# Operator Overloading in Python

## Summary

Operator overloading in Python allows you to define custom behavior for standard operators on user-defined classes. By implementing special methods, such as __add__, you can specify how operators like + should behave when applied to instances of your class. This feature leverages polymorphism by allowing operations to perform differently based on the type of objects they are applied to. This is particularly useful for making custom objects more intuitive and integrating them seamlessly with existing Python syntax.

## Docs

[Special Method Names](https://docs.python.org/3/reference/datamodel.html#special-method-names)
[Emulating Numeric Types](https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types)

## Examples

### Implementing operator overloading for addition:
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 4)
v2 = Vector(1, 3)
v3 = v1 + v2
print(v3)
# Output: Vector(3, 7)
```
### Customizing string representation:
```py
class Dragon:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"I am {self.name}, the {self.color} dragon"

jake = Dragon("Jake Long", "American")
print(jake)
# Output: I am Jake Long, the American dragon
```

## Operator Overload Review

| Operation             | Operator | Method         |
|-----------------------|----------|----------------|
| Addition              | +        | `__add__`      |
| Subtraction           | -        | `__sub__`      |
| Multiplication        | *        | `__mul__`      |
| Power                 | **       | `__pow__`      |
| Division              | /        | `__truediv__`  |
| Floor Division        | //       | `__floordiv__` |
| Remainder (modulo)    | %        | `__mod__`      |
| Bitwise Left Shift    | <<       | `__lshift__`   |
| Bitwise Right Shift   | >>       | `__rshift__`   |
| Bitwise AND           | &        | `__and__`      |
| Bitwise OR            | \|       | `__or__`       |
| Bitwise XOR           | ^        | `__xor__`      |
| Bitwise NOT           | ~        | `__invert__`   |
