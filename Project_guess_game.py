print("=================================")
print("=====TEBAK NOMOR TERSEMBUNYI=====")
print("=================================")
print("============= 0 - 9 =============")

nomor_tersembunyi = 9
jumlah_menjawab = 0
batas_menjawab = 3

while jumlah_menjawab < batas_menjawab:
    guess = int(input('Jawaban: '))
    jumlah_menjawab += 1
    if guess == nomor_tersembunyi:
        print("Kamu menang!")
        break
else:
    print("Sorry gan gagal")
