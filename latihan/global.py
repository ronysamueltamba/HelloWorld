nama = "Samuel"

def printNama():
    global nama
    nama += " Tamba"
    print(f'akses dari dalam {nama}')

printNama()
print(f'Akses dari luar {nama}')