class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):

    def bark(self):
        print("brak")

class Cat(Mammal):
    pass


dog1 = Dog()
dog1.bark()
