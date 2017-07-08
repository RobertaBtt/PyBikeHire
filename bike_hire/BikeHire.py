__author__ = 'roberta.btt@gmail.com'


class BikeHireSingleton:

    class __BikeHireSingleton:

        def __init__(self, arg):
            self.bike_dict = {}
            self.val = arg

        def __str__(self):
            return repr(self) + self.val
        instance = None

    def __init__(self, arg):
        if not BikeHireSingleton.__BikeHireSingleton.instance:
            BikeHireSingleton.instance = BikeHireSingleton.__BikeHireSingleton(arg)
        else:
            BikeHireSingleton.instance.val = arg

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def get_bike_by_id(self, bike_id):

        if self.bike_dict is not None:
            if bike_id in self.bike_dict:
                return self.bike_dict[bike_id]
            else:
                return None
        else:
            return None

    def add_bike(self, bike):
        self.bike_dict[bike.get_id()] = bike

    def get_bikes(self):
        return self.bike_dict