mulai = False
output = ""

while True:
    output = input("> ")
    if output.lower() == 'mulai':
        if mulai:
            print("Mobil Sudah Dijalankan...")
        else:
            mulai = True
            print("Mobil dijalankan")
    elif output.lower() == 'berhenti':
        if not mulai:
            print("Mobil sudah berhenti...")
        else:
            mulai = False
            print("Mobil berhenti")
    elif output.lower() == 'bantuan':
        print("""
        b -> bantuan
        m -> mulai
        s -> stop
        q -> quit
        """)
    elif output.lower() == 'quit':
        print('terima kasih')