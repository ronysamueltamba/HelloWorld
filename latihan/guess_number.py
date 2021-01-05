print('Guess The Number')

the_secret_number = 1
answer = 0
max_answer = 2

while answer < max_answer:
    guess = input('Guess: ')
    answer += 1
    if guess == the_secret_number:
        print(f"Yeay you win '_', the secret number is {the_secret_number}")
else:
    print("HAHAHAHA YOU LOSE :P")