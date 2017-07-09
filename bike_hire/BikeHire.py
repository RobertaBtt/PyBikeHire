__author__ = 'roberta.btt@gmail.com'


class BikeHireSingleton:

    class __BikeHireSingleton:

        def __init__(self):
            self.bike_dict = {}

        def __str__(self):
            return repr(self)
    instance = None

    def __init__(self):
        if not BikeHireSingleton.instance:
            BikeHireSingleton.instance = BikeHireSingleton.__BikeHireSingleton()


    def __getattr__(self, name):
        return getattr(self.instance, name)

    def add_bike(self, bike):
        self.bike_dict[bike.get_id()] = bike

    def get_bikes(self):
        return self.bike_dict

    def get_bike_by_id(self, bike_id):

        if self.bike_dict is not None:
            if bike_id in self.bike_dict:
                return self.bike_dict[bike_id]
            else:
                return None
        else:
            return None



