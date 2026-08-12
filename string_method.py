
#name = input("Enter your name: ")
#phone = input("Enter your phone #: ")

#name = len(name)
#result = name.find("a")
#result = name.rfind("a") # it find the result reversed 
#result = name.capitalize() # it capitalize the first letter of the word
#result = name.upper() # it capitalize the word entirely
#result = name.lower() # it makes it small letter words 
#result = name.isdigit() # it checks if it a number without alphabet
#result = name.isalpha() # it checks if the entire word is a is alpphabet without number
#result = phone.count("-")
#result = phone.replace("-", "")

# print(result)

# Validate User Input Exercise
#1. Username no more than 12 Characters
#2. Username must not contain spaces
#3. Username must not contain digits

username = input("Enter your username: ")

if len(username) > 12:
    print("Username can't contain more than 12 characters")
elif not username.find(" ") == -1:
    print("Username can't contain spaces")
elif not username.isalpha():
    print("Username can't contain digit")
else:
    print(f"Welcome {username}")