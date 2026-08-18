# Function = A block of reusable code, place() after the function name to invoke it


def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old")
    print("Happy birthday to you!")
    print()

happy_birthday("Jkagency", 22)
happy_birthday("Agbawo", 19)
happy_birthday("Bekke", 21)

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill is: #{amount} and is due on {due_date}")
    print()

display_invoice("Jkagency", 85000, "18/8/2026")


# Return = Statement used to end a function and send a result back to the caller

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1,2))
print(subtract(1,2))
print(multiply(1,2))
print(divide(1,2))
print()

# Example with Full name

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("Jkagency", "Agbawo")
print(full_name)
print()