from project.animals.animal import Bird
from project.food import Food, Meat, Vegetable, Fruit, Seed


class Owl(Bird):

    @property
    def type_of_food(self):
        return [Meat]

    @property
    def weight_gained(self):
        return 0.25

    @staticmethod
    def make_sound():
        return "Hoot Hoot"


class Hen(Bird):

    @property
    def type_of_food(self):
        return [Meat, Vegetable, Fruit, Seed]

    @property
    def weight_gained(self):
        return 0.35

    @staticmethod
    def make_sound():
        return "Cluck"
