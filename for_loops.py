#  For loops = Execute a block of code a fixed number of times. 
#              You can iterate over a range, string, sequence etc.

for x in range(1, 11):
    print(x)

# Range in reversed for countdown
for x in reversed(range(1, 11)):
    print(x)
print("Happy new year")

# Counting in 2's etc
for x in range(1, 11, 2):
    print(x)

credit_card = "1234-5678-9012-3456"

for x in credit_card:
    print(x)

# Skip  number 17
for x in range(1, 30):
    if x == 17:
        continue
    else:
        print(x)

# once it reach 18 it stop(break)
for x in range(1, 30):
    if x == 18:
        break
    else:
        print(x)

