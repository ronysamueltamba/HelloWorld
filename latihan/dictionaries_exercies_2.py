no_hp = input('Masukan no hp: ')
digit_mapping = {
    '1': 'satu',
    '2': 'dua',
    '3': 'tiga',
    '4': 'empat'
}

output = ""

for nomor in no_hp:
    output += digit_mapping.get(nomor, "!") + " "
print(output)