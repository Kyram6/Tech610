#1. variables - variables stores a value

name = "kyram" # string (str)
age = 23 #integer (int)
temperature = 15.7 #float
students = True #boolean
print(name,age,temperature)

#updating variables
count = 1
count = count + 1
#or
count += 1

#2. Collections - stores multiple values in order

#list
foods = ["pizza", "burger", "pasta"]
print(foods)

##loop through a list
for food in foods:
    print(food)

#Dictionary - stores key-value pairs
student = {
    "name":"kyram",
    "age": 23 }
print(student["name"])

##adding new key
student["course"] = "devops"

#Tuple - cannot be changed after creation 
    coordinates = (51.5, -0.1)
    ##tuple unpacking 
    latitude, longitude = coordinates
    print(latitude, longitude)

    #set = stores unique values 
    numbers = {1,2,3}

#control flow 
