import unittest
from bike_hire import  Bike
class BikeTestMethods(unittest.TestCase):

    def test_init(self):
        self.assertIsNotNone(Bike.Bike(1))

    def test_get_id(self):
        self.assertEqual(2, Bike.Bike(2).get_id())

    def test_get_average_duration(self):
        self.assertEqual(None, Bike.Bike(3).get_average_duration)


    def test_order_reporting_periods(self):
        self.assertEqual([], Bike.Bike(4)._order_reporting_periods())

if __name__ == '__main__':
    unittest.main()