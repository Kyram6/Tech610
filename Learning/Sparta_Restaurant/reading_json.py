import json
import sys
import os

if len(sys.argv) < 3:
    print("Usage: python reading_json.py <table_number> <dish>")
    sys.exit(1)

table = sys.argv[1]
dish = " ".join(sys.argv[2:]).strip().lower()

filename = "orders.json"

# load existing data
if os.path.exists(filename):
    with open(filename, "r") as file:
        orders = json.load(file)
else:
    orders = {}

table_name = f"Table {table}"

# create table if not exists
if table_name not in orders:
    orders[table_name] = []

# add dish
orders[table_name].append(dish)

# save
with open(filename, "w") as file:
    json.dump(orders, file, indent=2)

print("order saved")
