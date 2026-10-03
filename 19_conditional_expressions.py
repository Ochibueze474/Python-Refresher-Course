# Conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condition
#                          X if condition else Y

num = 4
print("Positive" if num > 0 else "Negative")

num_1 = 7
result =  "EVEN" if num_1 % 2 == 0 else "ODD"
print(result)

a = 7
b = 4

max_num =  a if a > b else b
print(max_num)

min_num = a if a < b else b
print(min_num)

age = 22
status =  "Adult" if age >= 18 else "Under Age"
print(status)

temp = 20
weather = "Hot" if temp > 20 else "Cold"
print(weather)

user_role = "guest"
access_level =  "Full access" if user_role == "admin" else "Limited Denied"
print(access_level)