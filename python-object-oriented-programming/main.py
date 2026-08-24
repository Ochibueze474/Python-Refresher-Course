
# object = A "bundle" of related attributes (variables) and methods(functions) Ex. phone, cup, book
#          You need a "class" to create many objects

# class = (blueprints) used to design the structure and layout of an object

from car import car

car1 = car("Lamborgini", 2026, "Black", True)
car2 = car("Lexus", 2027, "Red", False)
car3 = car("Ferrari", 2025, "Yellow", True)

print()
print(car2.model)
print(car2.year)
print(car2.colour)
print(car2.for_sale)
print()

car3.drive()
car3.stop()
print()

car1.describe()
print()