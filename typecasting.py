# Typecasting = the process of converting a variable from one data type to another
#               str(), int(), float(), bool()

name = "Jkagency"
name_1 = ""
age = 22
gpa = 3.2
is_student = False


gpa = int(gpa)
print(type(age))
print(gpa)

name = bool(name)
print(type(name))
print(name) # When converted to boolean when there is a name in the string or when its not empty its shows TRUE

name_1 = bool(name_1)
print(type(name_1))
print(name_1) # When converted to boolean when the string is empty it shows FALSE 

age = str(age)
print(type(age)) 
age += 1 # It shows TypeError: can only concatenate str (not "int") to str
age += "1" # It add to it as a string and not int 
print(age)

age = float(age)
print(type(age))
print(age)
