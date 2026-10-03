# 2D Collection

fruits = ["Apple", "Orange", "Banana", "Coconut"]
vegetables = ["Celery", "Carrots", "Potatos"]
meats = ["Chicken", "Fish", "Turkey"]

groceries = [fruits, vegetables, meats]

print(groceries[0][1])


# Using nested loop

skillset = [["Python", "SQL", "VBA", "DAX"],
["Excel", "Power BI", "PostgreSQL"],
["Upwork", "LinkedIn", "micro1"]]

for collection in skillset:
    for tool in collection:
        print(tool, end= " ")
    print()


# Dial pad
num_pad = ((1, 2, 3), 
           (4, 5, 6), 
           (7, 8, 9), 
           ("*", 0, "#" ))

for row in num_pad:
    for num in row:
        print(num, end= " ")
    print()
