class Mammal:
    def walk(self):
        print('Walk')


class Dog(Mammal):
    def bark(self):
        print('Bark')


class Cat(Mammal):
    def be_annoying(self):
        print('annoying')


dog1 = Dog()
dog1.walk