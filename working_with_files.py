file = open("Sparta_Restaurant/order.txt", "w")
orders = [
    "Chocolate",
    "Chips",
    "Mayo",
    "waffles",
    "rice",
]

file.write('\n'.join(orders))
file.write('\n')

print(file)

file.close()

#w overwrites itself
#a+ for append add on
#r reads