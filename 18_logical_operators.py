#Logical operators = evaluate multiple conditions (or, and, not)
#                  or = atleast one condition must be True
#                  and = both conditions must be True
#                  not = inverts the condition (not False, not True)

# OR
temp = 30
is_raining = True

if temp > 35 or temp < 5 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")

# AND with Not operator
temp = 18
is_sunny = False

if temp >= 28 and is_sunny:
    print("It's Hot outside")
    print("It's Sunny")
elif temp <= 18 and is_sunny:
    print("It's Cold outside")
    print("It's Sunny")
elif temp < 28 and temp > 18 and is_sunny:
    print("It's Warm outside")
    print("It's Sunny")
elif temp >= 28 and not is_sunny:
    print("It's Hot outside")
    print("It's Cloudy")
elif temp <= 18 and not is_sunny:
    print("It's Cold outside")
    print("It's Cloudy")
elif temp < 28 and temp > 18 and not is_sunny:
    print("It's Warm outside")
    print("It's Cloudy")