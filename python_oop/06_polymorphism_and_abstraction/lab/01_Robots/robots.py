import random
from abc import ABC, abstractmethod


class Robot(ABC):
    def __init__(self, name):
        self.name = name

    @staticmethod
    @abstractmethod
    def sensors_amount():
        pass


class MedicalRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 6


class ChefRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 4


class WarRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 12

    @classmethod
    def random_name(cls):
        name = f"Robo{random.randint(1, 100)}"
        return cls(name)


da_vinci = MedicalRobot('Da Vinci')
moley = ChefRobot('Moley')
griffin = WarRobot('Griffin')

for r in [da_vinci, moley, griffin]:
    print(r.sensors_amount())

r = WarRobot.random_name()
print(r.name)
