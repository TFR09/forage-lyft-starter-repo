import unittest

from carrigan_tires import CarriganTires

class TestCarriganTires(unittest.TestCase):
    def tires_should_be_serviced(self):
        tires = [0.9, 0.9, 0.9, 0.9]
        tire = CarriganTires(tires)
        
        self.assertTrue(tire.needs_service())

    def tires_should_not_be_serviced(self):
        tires = [0.89, 0.89, 0.89, 0.89]
        tire = CarriganTires(tires)

        self.assertFalse(tire.needs_service())