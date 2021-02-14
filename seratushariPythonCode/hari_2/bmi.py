tinggi = float(input("Masukan tinggi kamu dalam (m): "))
berat_badan = int(input("Masukan berat badan kamu: "))

bmi = round(berat_badan / tinggi**2)

print(bmi)