print("Welcome to the rollercoaster")
height = int(input("What is your height? "))
bill = 0
extras_photo = 3

if height >= 120:
    print("You can ride a rollercoaster")
    age = int(input("Input your age? "))
    if age > 18:
        bill = 12
        print("Adult tickets are $12")
    elif age > 12:
        bill = 7
        print("Young tickets are $7")
    else:
        bill = 5
        print("Child tickets are $5")
    print("Take photos add $3")
    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo.upper() == "Y":
         bill += extras_photo
         print(f"Your final bill is {bill}")
    elif wants_photo.upper() == "N":
        print(f"Your final bill is {bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")