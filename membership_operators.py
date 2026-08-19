# Membership operator = used to test whether a value or variable is found in a sequence(string, list, tuple, set, or dictionary)
#                       1. in
#                       2. not in


# IN example
word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter in word:
    print(f"There is {letter}")
else:
    print(f"{letter} was not found")

print()


# IS NOT example
students = {"Jkagency", "Agbawo", "Crazyworld"}

student = input("Enter the name of a student: ")

if student not in students:
    print(f"{student} is not a student")
else:
    print(f"{student} is a student")

print()

# Another example using dictionary
grades = {"Sandy": "A",
          "Squidward": "B",
          "Spongebob": "C",
          "Patrick": "D"}

student = input("Enter the name of a student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")

print()

# Another example using 'and' in the membership operator 
email = "Jkagency@gmail.com"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")