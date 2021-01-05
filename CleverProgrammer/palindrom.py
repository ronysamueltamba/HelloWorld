palindrom = input('Cek palindrom: ')
rev_palindrom = palindrom[::-1]

if palindrom == rev_palindrom:
    print('Kata ini adalah palindrom')
else:
    print('Kata ini bukan palindrom')