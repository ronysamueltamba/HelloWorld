nama = input('Masukan nama kamu: ')

if len(nama) < 3:
    print(f'Namamu {nama} ')
    print('nama setidaknya 3 character')
elif len(nama) > 20:
    print(f'Namamu {nama}')
    print(len('Nama terlalu panjang, maksimal 20 character'))
    print(f'Namamu berjumlah {len(nama)} character')
else:
    print(f'{nama}')
    print(f'Mantap slur, nama berjumlah {len(nama)} character')