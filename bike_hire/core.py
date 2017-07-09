__author__ = 'roberta.btt@gmail.com'

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

        for key, bike in bike_dict.iteritems():
            average_duration = bike.get_average_duration
            if average_duration is not None:
                average_duration_total += average_duration
                num_rides_to_avg += 1

        if num_rides_to_avg != 0:
            average_journey_duration = average_duration_total / num_rides_to_avg
        else:
            average_journey_duration = 0
        print "The average journey duration is: " , average_journey_duration

    def __build_data(self):



        bike_dict = {}
        lines = self.read_lines()

        for line in lines:
            elements = line.split("," )

            bike_id = elements[1]

            bike = self.bike_hire.get_bike_by_id(bike_id)
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


                self.bike_hire.add_bike(bike)

    def read_lines(self):

        with open(self.file_path) as f:
            lines = f.readlines()
        lines = [x.strip() for x in lines]

        return lines

#====================================
if __name__ == '__main__':
    file_path = "data.csv"

    bikeHireProject = BikeHireProject(file_path)