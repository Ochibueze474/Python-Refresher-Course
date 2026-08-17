# Concession Stand Program

menu = {"ofe onugbu": 3500,
        "ofe oha": 4000,
        "ofe egusi": 2500,
        "amala ati ewedu": 3000,
        "ofe okro": 2000,
        "ofe akwu": 1500,
        "beans": 1000,
        "rice": 1000}

cart = []
total = 0

print("---------- MENU -----------")
for key, value in menu.items():
    print(f"{key:20}: #{value}")
print("---------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("-------- YOUR ORDER -------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"The Total is: #{total}")


