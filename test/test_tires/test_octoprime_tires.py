import unittest

from octoprime_tires import OctoprimeTires

class TestCarriganTires(unittest.TestCase):
    def tires_should_be_serviced(self):
        tires = [0.75, 0.75, 0.75, 0.75]
        tire = OctoprimeTires(tires)
        
        self.assertTrue(tire.needs_service())

    def tires_should_not_be_serviced(self):
        tires = [0.75, 0.75, 0.75, 0.74]
        tire = OctoprimeTires(tires)

        self.assertFalse(tire.needs_service())