__author__ = 'RobertaBtt'
import pathlib
from datetime import datetime,date,timedelta
import Bike
import BikeHire


class BikeHireProject():

    def __init__(self, file_path):

        self.file_path = file_path
        self.bike_hire = BikeHire.BikeHireSingleton()
        self.print_average_journey_duration()

    def print_average_journey_duration(self):

        self.__build_data()
        bike_dict = self.bike_hire.get_bikes()
        num_rides_to_avg = 0
        average_duration_total = timedelta()

        for key, bike in bike_dict.items():
            average_duration = bike.get_average_duration()
            if average_duration is not None:
                average_duration_total += average_duration
                num_rides_to_avg += 1

        if num_rides_to_avg != 0:
            average_journey_duration = average_duration_total / num_rides_to_avg
        else:
            average_journey_duration = 0
        print("The average journey duration is: ", average_journey_duration)


    def __build_data(self):
        """
        Constructs data from .csv lines
        :return:
        """
        try:
            with open(file_path) as f:
                lines = f.readlines()
            lines = [x.strip() for x in lines]
            for line in lines:
                elements = line.split(",")
                bike_id = elements[1]
                bike = self.bike_hire.get_bike_by_id(bike_id)
                bike = BikeHireProject._add_reporting_data(bike, elements, bike_id)
                self.bike_hire.add_bike(bike)
        except (RuntimeError):
            print("Please check the format of the csv file")

    @staticmethod
    def _add_reporting_data(bike, elements, bike_id=None):
        """

        :param bike: The instance of the class Bike in which I'm adding list of reporting journey
        :param elements: list of string
        :param bike_id: id of a Bike
        :return: a new instance of a Bike, or the same modified by adding reporting list
        """

        if bike is not None:
            if str(elements[2]) != '':
                bike.add_reporting_period('A' + str(elements[2]))
            if str(elements[3]) != '':
                bike.add_reporting_period('D' + str(elements[3]))
        else:
            bike = Bike.Bike(bike_id)
            if str(elements[2]) != '':
                bike.add_reporting_period('A' + str(elements[2]))
            if str(elements[3]) != '':
                bike.add_reporting_period('D' + str(elements[3]))

        return bike


#====================================
if __name__ == '__main__':
    file_path = str(pathlib.Path().absolute())+"/bike_hire/data.csv"
    bikeHireProject = BikeHireProject(file_path)