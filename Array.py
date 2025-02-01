#array
cars = ["Ford", "Volvo", "BMW"]
print(cars)

#Access the Elements of an Array
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)

cars = ["Ford", "Volvo", "BMW"]
cars[0] = "Toyota"
print(cars)

#The Length of an Array
cars = ["Ford", "Volvo", "BMW"]
x = len(cars)
print(cars)

#Looping Array Elements
cars = ["Ford", "Volvo", "BMW"]
for x in cars:
    print(x)

#Adding Array Elements
cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print(cars)

#Removing Array Elements
cars = ["Ford", "Volvo", "BMW"]
cars.pop(1)
print(cars)

cars = ["Ford", "Volvo", "BMW"]
cars.remove("Volvo")
print(cars)