#No8
class Animal:
    def make_sound():
        return 'some animal sound'

class Cat(Animal):
    def make_sound():
        return 'Meow'

a1 = Animal
c1 = Cat
print(a1.make_sound(),'\n',c1.make_sound())