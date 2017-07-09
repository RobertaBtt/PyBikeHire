__author__ = 'roberta.btt@gmail.com'

import datetime
from datetime import timedelta

class Bike:

    def __init__(self, bike_id):
        self.reporting_period_list = []
        self.average_duration = 0
        self.bike_id = bike_id

    def get_id(self):
        return self.bike_id

    def add_reporting_period(self, reporting_period_string):
        self.reporting_period_list.append(reporting_period_string)

    def get_reporting_period_list(self):
        return self.reporting_period_list

    def get_average_duration(self):

        data_format = '%Y%m%dT%H:%M:%S'
        temp_index_departure = -1
        num_rides = 0
        to_calculate = False
        tdelta = timedelta()

        ordered_reporting_list = self._order_reporting_periods()
        for idx, val in enumerate(ordered_reporting_list):
            print(idx, val)

            if val[0] == 'D':
                temp_index_departure = idx
                to_calculate = True
            elif val[0] == 'A':
                if to_calculate:
                    tdelta += datetime.datetime.strptime(ordered_reporting_list[idx][1:], data_format) - \
                             datetime.datetime.strptime(ordered_reporting_list[temp_index_departure][1:], data_format)
                    num_rides += 1
                    to_calculate = False

        if num_rides !=0:
            average_rides_duration = tdelta / num_rides
        else:
            average_rides_duration = None

        return average_rides_duration

    def _order_reporting_periods(self):
        try:
            return sorted(self.reporting_period_list, key=lambda x: datetime.datetime.strptime(x[1:], '%Y%m%dT%H:%M:%S'))
        except (ValueError):
            print "Check data format (%Y%m%dT%H:%M:%S)"
            return None
