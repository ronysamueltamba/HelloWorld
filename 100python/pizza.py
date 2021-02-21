print("Welcome to Pizza Deliveries")
size = input("What size do you want? S, M, or L? ")
add_papperoni = input("Do you wnat papperoni? Y or N? ")
extra_cheese = input("Do you want extra cheese? Y or N? ")

bill = 0

if size.upper() == 'S':
    bill += 15
elif size.upper() == 'M':
    bill += 20
else:
    bill += 25

if add_papperoni.upper() == 'Y':
    if size.upper() == 'S':
        bill += 2
    else:
        bill += 3

if extra_cheese.upper() == 'Y':
    bill += 1

print(f"Total bil you pay ${bill}")

