name = input('Nama monsternya siapa? ')
monster = {"name": name, 'power':100}

def startGame():
    choice = input('Mau apa? 1. Makan 2. Lihat Status 3. Keluar')
    if choice == '1':
        goEat()
    elif choice == '2':
        goStatus()
    else:
        goExit()

def goEat():
    print('Nyam.. Nyam..')
    monster['power'] += 100
    startGame()

def goStatus():
    print('Cek.. Cek..')
    print(monster)
    startGame()

def goExit():
    print('Bye.. Bye..')

startGame()