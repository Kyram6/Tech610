# Python Challenges for IO Scripts:
#1. Python Script that accepts a menu order as an argument,
# and appends it to orders.txt.
# How are spaces handled in dish names? e.g chicken fried rice

import sys
args = sys.argv
if len(sys.argv) < 2: #no order supplied if less than 2 arg
    print("no order taken")
    sys.exit(1)

#taking order ignore name of script
order = " ".join(sys.argv[1:]).strip() #joins words with spaces " " # : everything after one

#opening order.txt file
with open ("order.txt", "a") as file: #with closes file when done and a appends
    file.write(order + '\n') # adding new line

print("order taken")
