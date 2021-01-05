class informatika():
    def __init__(self, name, kelas, nrp):
        self.nama = name
        self.kelas = kelas
        self.nrp = nrp


rony = informatika('Rony Samuel Tamba', '4IF-01', 170613055)
arifin = informatika('Arifin Steven Sitanggang', '4IF-01', 170613092)
zakha = informatika('Zakharia', '4IF-01', 170613023)

print(rony.__dict__, arifin.__dict__, zakha.__dict__)
