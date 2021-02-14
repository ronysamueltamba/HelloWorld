tahun = int(input("Masukan tahun yang akan dicek: "))

if tahun % 4 == 0:
    if tahun % 100 == 0:
        if tahun % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")