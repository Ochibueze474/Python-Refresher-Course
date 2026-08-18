# Default arguments = A default value for certain parameters default is used when that argument is omitted make your functions more flexible, reduces # of arguments 
# 1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

# Positional example
def net_price(list_price, discount, tax):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500, 0, 0.05))
print()

#Default example reduces # of argument
def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500))
print(net_price(500, 0.1)) # if a coupon discount is given off 10% then it can be added manually
print(net_price(500,0.10,0)) # if there is not tax added then you can add 0 manually thats its not added
print()


import time

def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done!")

count(20,10)
print()

