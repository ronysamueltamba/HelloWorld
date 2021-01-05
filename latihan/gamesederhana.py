player1 = {'name': 'songoku', 'power':100}
player2 = {'name': 'trunk', 'power':250}

# fungsi player bisa training
def train(player):
    player['power'] += 100

# fungsi menyerang
def attack(attacker, defender):
    if(attacker['power'] > defender['power']):
        print(f'Serangan berhasil, selamat untuk', attacker['name'])
    else:
        print('Serangan gagal', attacker['name'])

train(player1)
train(player1)
attack(player1, player2)