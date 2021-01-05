umur = int(input('Masukan tahun kelahiran kamu: '))
checker = 2020 - umur

if checker >= 50:
    print(f'Umur anda {checker} tahun')
    print('Anda tergolong lansia')
elif checker >= 40:
    print(f'Umur anda {checker} tahun')
    print('Anda tergolong bapack-bapack')
elif checker >= 20:
    print(f'Umur anda {checker} tahun')
    print('Anda masih muda, yok berusaha sukses!')
else:
    print(f'Umur kamu masih {checker} tahun')
    print('Masih bocil awkoawkoakwo')