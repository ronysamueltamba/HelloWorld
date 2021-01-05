weight = int(input('Weight: '))
pilih = input('(K)g or (L)bs: ')

if pilih.lower() == 'k':
    weight /= 0.45
    print(f'Weight in Lbs {weight}')
elif pilih.lower() == 'l':
    weight *= 0.45
    print(f'Weight in Lbs {weight}')