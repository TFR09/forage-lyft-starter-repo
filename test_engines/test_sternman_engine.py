import unittest

from engines.sternman_engine import SternmanEngine

class TestSternmanEngine(unittest.Testcase):
    def test_engine_should_not_be_serviced(self):
        is_warning_light_on = False
        engine = SternmanEngine(is_warning_light_on)
        self.assertFalse(engine.needs_service())
    
    def test_engine_should_be_serviced(self):
        is_warning_light_on = True
        engine = SternmanEngine(is_warning_light_on)
        self.assertTrue(engine.needs_service())