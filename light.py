# import time
# while True:
#     print("Red")
#     time.sleep(5)
#     print("Green")
#     time.sleep(4)
#     print("Yellow")
#     time.sleep(2)
# import random
# weather = ["Sunny", "Cloudy","Rainy"]
# print("================================")
# print("       WEATHER SIMULATION       ")
# print("================================")
# for day in range(1, 8):
#     today_weather = random.choice(weather)
# print("Weather: ", today_weather)
# print("---------------------------------")
# print("Simulation Completed.")

# population = 1000
# growth_rate = 0.10
# for year in range(1, 6):
#     population = population + (population * growth_rate)
# print("Year:",year)
# print("Population:", int(population))
# print("-----------")


# Bank service simulation model
import time
customers = ["A" , "B" , "C" , "E"]
print("Bank Service Simulation\n")
for customer in customers:
    print(customer, "arrived")
    print("Serving", customer)