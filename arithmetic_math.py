friends = 10

#friends = friends + 1
#friends += 1
#friends = friends - 4
#friends -= 4
#friends = friends * 3
#friends *= 3
#friends = friends ** 2
#friends **= 2
remainder = friends % 3


print(remainder)

x = 1.47
y = -4
z = 7

#result = round(x)
#result = abs(y)
#result = pow(z, 2)
#result = max(x, y, z)
result = min(x, y, z)

print(result)

import math

print(math.pi)
print(math.e)

a = 9
b = 9.1
c = 9.9

answer = math.sqrt(a) 
answer_1 = math.ceil(b)
answer_2 = math.floor(c)

print(answer)
print(answer_1)
print(answer_2)

radius = float(input("Enter the radius of the circle: "))

circumference = 2 * math.pi * radius

print(f"The Circumference is: {round(circumference, 2)}cm")

radius = float(input("Enter the radius of the circle: "))

area = math.pi * pow(radius, 2)

print(f"The area of the circle is: {round(area, 2)}cm^2")


a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side C: {round(c, 2)}")