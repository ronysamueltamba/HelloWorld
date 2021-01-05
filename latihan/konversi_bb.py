weight = int(input('Masukan berat badan kamu: '))
pilih = input('Pilih (L)bs atau (K)g : ')

if pilih.upper() == "L":
    conversi = weight * 0.45
    print(f'Berat badan kamu adalah {conversi} Kg')
elif pilih.upper() == "K":
    conversi = weight / 0.45
    print(f'Berat badan kamu adalah {conversi} Lbs')
