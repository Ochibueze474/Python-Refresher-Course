# Format specifiers = {value:flags} format a value based on what flags is inserted

price1 = 7204.667
price2 = -9404.67
price3 = 3444.66

#for 2 decimal place
print(f"The price for price1 is: {price1:.2f}")
print(f"The price for price2 is: {price2:.2f}")
print(f"The price for price3 is: {price3:.2f}")

# for 3 decimal place
print(f"The price for price1 is: {price1:.3f}")
print(f"The price for price2 is: {price2:.3f}")
print(f"The price for price3 is: {price3:.3f}")

# A thousand separator format
print(f"The price for price1 is: {price1:,}")
print(f"The price for price2 is: {price2:,}")
print(f"The price for price3 is: {price3:,}")

# Right sided space
print(f"The price for price1 is: ${price1:10}")
print(f"The price for price2 is: ${price2:10}")
print(f"The price for price3 is: ${price3:10}")

# 0 parted
print(f"The price for price1 is: ${price1:010}")
print(f"The price for price2 is: ${price2:010}")
print(f"The price for price3 is: ${price3:010}")

# Left sided space 
print(f"The price for price1 is: ${price1:<10}")
print(f"The price for price2 is: ${price2:<10}")
print(f"The price for price3 is: ${price3:<10}")

# Placed in the middle
print(f"The price for price1 is: ${price1:^10}")
print(f"The price for price2 is: ${price2:^10}")
print(f"The price for price3 is: ${price3:^10}")

# Adding positive sign
print(f"The price for price1 is: ${price1:+}")
print(f"The price for price2 is: ${price2:+}")
print(f"The price for price3 is: ${price3:+}")

# Adding positive, thousand seprator and 2 decimal place in the flag
print(f"The price for price1 is: ${price1:+,.2f}")
print(f"The price for price2 is: ${price2:+,.2f}")
print(f"The price for price3 is: ${price3:+,.2f}")