# List comprehension = A concise way to create lists in python, Compact and easier to read than traditional loops
#                      [expression for value in iterables if condition]

doubles = []

for x in range(1, 11):
    doubles.append(x * 2)

print(doubles)
print()

# Instead of this up here 
doubles = [x * 2 for x in range(1, 11)]
triples = [y * 3 for y in range(1, 11)]
squares = [z * z for z in range(1, 11)]
print(doubles)
print(triples)
print(squares)
print()

# Using list with strings as example 
fruits = ["apple", "banana", "orange", "coconut"]

fruit = [fruit.capitalize() for fruit in fruits]
print(fruit)
print()

# Using list with numbers as example
numbers = [1, -2, -3, 4, 6, -8, 7, -5]

positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]

print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)

print()

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grade = [grade for grade in grades if grade >= 60]

print(passing_grade)