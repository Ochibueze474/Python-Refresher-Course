# input() = A function that prompts the user to enter data
#           Returns the entered data as a string

name = input("What is your name?: ")
age = int(input("How old are you?: ")) # its need to converted first to int unless its going to show TypeError: can only concatenate str (not "int") to str

age = age + 1

print(f"Hello {name}")
print("Happy Birthday!")
print(f"You are {age} years old")

# Exercise 1 Rectangular Area Calc
 
Length = float(input("Enter The Lenght: "))
Width = float(input("Enter the Width: "))

area = Length * Width

print(f"The area is: {area}cm²")

#Exercise 2 shopping cart program

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${total}")