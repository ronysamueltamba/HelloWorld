output = ""
started = False

while True:
    output = input('> ')
    if output == 'start':
        if started:
            print('Engine already started!!!')
        else:
            started = True
            print('Engine started...')
    elif output == 'stop':
        if not started:
            print('Engine already stop!!!')
        else:
            started = False
            print('Engine stop...')
    elif output == 'help':
        print('''
        start -> to start
        stop  -> to stop
        help  -> help
        quit  -> quit
        ''')
    elif output == 'quit':
        print("Thank's")
        break