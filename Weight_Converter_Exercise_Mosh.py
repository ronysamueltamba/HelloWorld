weight = int(input("Weight: "))
pilihan = input("(L)bs or (K)g: ")

if pilihan.upper() == "L":
    converted = weight * 0.45
    print(f"Your weight is {converted} Lbs")
elif pilihan.upper() == "K":
    converted = weight / 0.45
    print(f"Your weight is {converted} Kg")


