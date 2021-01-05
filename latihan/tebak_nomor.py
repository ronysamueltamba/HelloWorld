print('======================================')
print('========GUESS THE NUMBER GAMES========')
print('======================================')
print('==========RANGE 700 - 999=============')

secret_number = 777
answer = 0
max_answer = 3

the_answer_is = 0

while answer < max_answer:
    the_answer_is = int(input('Guess the secret number: '))
    answer += 1
    if the_answer_is == secret_number:
        print(f'Yeay, congrats! {secret_number} is a secret number')
        break
    elif the_answer_is > 999:
        print('maximum of number is 999')
else:
    print('Nah, you failed')

print('======================================')
print('Wanna try again? ')
play_again = input('(Y)es or (N)ot? ')
print('======================================')

while the_answer_is:
    if play_again.upper() == 'y':
        print(the_answer_is)