weight = int(input("Weight: "))
pilihan = input("(L)bs or (K)g: ")

if pilihan == "L" or "l":
    print("You are ", weight * 0.45, "Kg")
elif pilihan == "K" or "k":
    print(f"You are {weight / 0.45} Lbs")


