# Polymorphism Through Method Overriding in Python

## Summary

Polymorphism in Python allows objects to be treated as instances of their parent class. This can be achieved through method overriding, where child classes have methods with the same name as their parent class but with different implementations. It enables the same method to exhibit different behaviors depending on the object it is acting upon, thus allowing for more flexible and reusable code.

## Docs

[Polymorphism](https://en.wikipedia.org/wiki/Polymorphism_(computer_science))

## Examples

### Demonstrating polymorphism with a creature hierarchy:
```python
class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def sound(self):
        print("Woof woof!")

class Cat(Animal):
    def sound(self):
        print("Meow!")

animals = [Animal(), Dog(), Cat()]

for animal in animals:
    animal.sound()
# Outputs:
# Some generic animal sound
# Woof woof!
# Meow!
```