# Variables = A container for a value (string, integer, float, boolean)
#             A variable behaves as if it was the value it contains

#Strings
first_name = "Jkagency"
food = "Ofe Onugbu"
email = "Jkagency@gmail.com"

print(f"My name is {first_name}")
print(f"My favourite food is {food}")
print(f"Contact me throught me email: {email}")

#Integers
age = 22
quantity = 4
num_of_students = 70

print(f"You are {age} years old")
print(f"You are to buy {quantity} items")
print(f"There are {num_of_students} pupils in SS1 class")

#Floats
price = 30999.99
gpa = 3.2
distance = 5.5

print(f"The cylinder cost #{price}")
print(f"Your gpa is: {gpa}")
print(f"He ran {distance}km")

#Booleans
is_student = True
for_sale = False
is_online = True


if is_student:
    print("You are a student")
else:
    print("You are not a student")

if for_sale:
    print("That item is for sale")
else:
    print("That item is not available")

if is_online:
    print("You are online")
else:
    print("You are Offline")