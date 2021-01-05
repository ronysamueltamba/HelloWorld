class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, I am {self.name}")


sam = Person("Samuel")
sam.talk()

tam = Person('Tamba')
tam.talk()