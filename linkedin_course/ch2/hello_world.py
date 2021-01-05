def main():
    nomor_rahasia = 777
    jawaban = 0
    max_jawab = 3

    while jawaban < max_jawab:
        adalah = int(input('Tebak nomor: '))
        jawaban += 1
        if adalah == nomor_rahasia:
            print(f'Wow tebakanmu benar! yaitu {nomor_rahasia}')
            break
    else:
        print('Jawabanmu belum benar nih')


if __name__ == "__main__":
    main()
