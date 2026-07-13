#A separate script that accepts orders.txt
# and prints out how many times
#each dish has been ordered.
#import sys
#import json

#args = sys.argv
#if len(sys.argv) < 2: #no order supplied if less than 2 arg
    #print("no file")
    #sys.exit(1)

#filename = sys.argv[1]
#try: # code that might cause an error
    #with open(filename, "r") as file: #r = read file
        #orders = json.load(file) #reads file into list
#except FileNotFoundError: # what to do if error happens
    #print("Not Found")
    #sys.exit(1)

#counting orders
#counts = {}

#for dishes in orders.values:
    #for dish in dishes:
    #dish = dish.strip().lower() #removes whitespace and so capital still counts

    #if dish:
        #if dish in counts:
            #counts[dish] += 1
        #else:
            #counts[dish] = 1

#print("Full Order")
#for dish, count in counts.items():
    #print(f"{dish}: {count}")

# dictionary name square brackets key - to find things in a dictionary
# e.g print(order["chicken"])

import json
import sys

if len(sys.argv) < 2:
    print("Use: python count_orders.py orders.json") #if forget file
    sys.exit(1)

filename = sys.argv[1]

with open(filename, "r") as file:
    orders = json.load(file)

print("\nFULL ORDER SUMMARY")

counts = {}

# count all dishes
for dishes in orders.values():
    for dish in dishes:
        counts[dish] = counts.get(dish, 0) + 1

for dish, count in counts.items():
    print(f"{dish}: {count}")

print("\nORDERS BY TABLE")

# show per table
for table, dishes in orders.items():
    print(f"\n{table}:")
    for dish in dishes:
        print(f" - {dish}")