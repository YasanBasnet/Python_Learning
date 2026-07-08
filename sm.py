import random
stock = 100
for day in range (1 ,6 ):
    demand = random.randint(10,20)
    stock -= demand
    print(f"Day {day}")
    print(f"Demand: {demand}")
    print(f"Remaining Stock: {stock}\n")
