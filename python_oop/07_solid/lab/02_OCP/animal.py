from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        return 'meow'


class Dog(Animal):
    def make_sound(self):
        return 'woof-woof'


class Duck(Animal):
    def make_sound(self):
        return "quack"


class Chicken(Animal):
    def make_sound(self):
        return "cluck-cluck"


def animal_sound(animals_list):
    for animal in animals_list:
        print(animal.make_sound())


animals = [Cat('Kitty'), Dog("Lucky"), Duck("Lucy"), Chicken("Chick")]
animal_sound(animals)


## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
