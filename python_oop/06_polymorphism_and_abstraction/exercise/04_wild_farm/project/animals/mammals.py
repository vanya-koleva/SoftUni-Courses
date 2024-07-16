from project.animals.animal import Mammal
from project.food import Food, Vegetable, Fruit, Meat


class Mouse(Mammal):

    @property
    def type_of_food(self):
        return [Vegetable, Fruit]

    @property
    def weight_gained(self):
        return 0.10

    @staticmethod
    def make_sound():
        return "Squeak"


class Dog(Mammal):

    @property
    def type_of_food(self):
        return [Meat]

    @property
    def weight_gained(self):
        return 0.40

    @staticmethod
    def make_sound():
        return "Woof!"


class Cat(Mammal):

    @property
    def type_of_food(self):
        return [Meat, Vegetable]

    @property
    def weight_gained(self):
        return 0.30

    @staticmethod
    def make_sound():
        return "Meow"


class Tiger(Mammal):

    @property
    def type_of_food(self):
        return [Meat]

    @property
    def weight_gained(self):
        return 1.00

    @staticmethod
    def make_sound():
        return "ROAR!!!"
