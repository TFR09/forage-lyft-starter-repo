from abc import ABC
from .tire import Tire

class OctoprimeTires(Tire, ABC):
    def __init__(self, tires):
        self.tires = tires

    def needs_service(self):
        total_worn_out = 0
        for tire in self.tires:
            total_worn_out += tire
        return total_worn_out >= 3
