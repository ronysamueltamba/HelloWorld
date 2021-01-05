name = input("Masukan nama: ")

if len(name) <= 3:
    print("Name must be at least 3 character")
elif len(name) > 20:
    print("Name can be a maximum 20 character")
    print("That have", len(name), "Characters")
else:
    print("Name looks good")
    print("Memiliki", len(name), "Character")