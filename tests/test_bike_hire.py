import unittest
from bike_hire import BikeHire, Bike


class BikeHireTestMethods(unittest.TestCase):

    def test_singleton_class(self):
        bike_hire_instance_1 = BikeHire.BikeHireSingleton()
        bike_hire_instance_2 = BikeHire.BikeHireSingleton()
        self.assertEqual(bike_hire_instance_1.instance, bike_hire_instance_2.instance)

    def test_add_bike(self):
        bike_hire = BikeHire.BikeHireSingleton()
        bike_hire.add_bike(Bike.Bike(2))
        self.assertEqual(1, len(bike_hire.get_bikes()))

    def test_get_by_by_id(self):
        bike_hire = BikeHire.BikeHireSingleton()
        bike_hire.add_bike(Bike.Bike(2))
        self.assertIsNotNone(bike_hire.get_bike_by_id(2))
        self.assertIsNone(bike_hire.get_bike_by_id(3))


if __name__ == '__main__':
    unittest.main()