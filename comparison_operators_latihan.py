temperature = input("Berapa derajat suhu hari ini: ")

if int(temperature) >= 30:
    print("Wow it's a hot day")
elif int(temperature) < 10:
    print("Wow it's a cold day")
else:
    print("It's neither hot nor cold")