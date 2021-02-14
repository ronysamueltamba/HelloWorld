tinggi = float(input("Masukan tinggi kamu dalam (m): "))
berat_badan = int(input("Masukan berat badan kamu: "))

tinggi = tinggi / 100

bmi = round(berat_badan / tinggi**2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you are normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
else:
    print(f"Your BMI is {bmi}, you are obese")