# Inheritance in Python

## Summary

Inheritance is a feature in object-oriented programming that allows a "child" class to inherit the properties and methods of a "parent" class. This promotes code reuse and helps prevent redundancy, adhering to the DRY (don't repeat yourself) principle. In Python, inheritance is implemented by defining a class with the syntax class ChildClass(ParentClass):. The super() function is used to call the parent class's constructor within the child class, allowing the child class to initialize the inherited properties.

Inheritance should be used judiciously; it is most appropriate when the relationship between the parent and child classes is truly an "is-a" relationship, meaning every instance of the child class is also an instance of the parent class.

## Docs

[Inheritance] (https://docs.python.org/3/tutorial/classes.html#inheritance)\
[super()] (https://docs.python.org/3/library/functions.html#super)

## Examples

## Basic inheritance and using super():
```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

my_car = Car("Toyota", "Camry")
print(my_car.brand)  # Toyota
print(my_car.model)  # Camry
```

### Illustrating the concept of "is-a" relationship:
```python
class Electronic:
    def __init__(self):
        self.power_source = "electricity"

class Laptop(Electronic):
    def __init__(self, brand):
        super().__init__()
        self.brand = brand

laptop = Laptop("Apple")
print(laptop.power_source)  # electricity
print(laptop.brand)         # Apple
```