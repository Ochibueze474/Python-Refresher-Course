# Random Numbers  

import random

low = 1
high = 20
options = ("Rock", "Paper", "Scissors")
cards = ["2","3","4","5","7","8","10","11","12","13","14","20"]

number = random.randint(low, high)
random_number = random.random() # This pick random numbers within 0 and 1
option = random.choice(options)
random.shuffle(cards) # This shuffles card or shuffles things


print(number)
print(random_number)
print(option)
print(cards) 