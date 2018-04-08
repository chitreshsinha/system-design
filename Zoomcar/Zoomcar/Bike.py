from Vehicle import Vehicle

class Bike(Vehicle):

    def __init__(self, name, rank, kms_travelled, lat, lng):
        super(Bike, self).__init__("Bike", name, rank, kms_travelled, lat, lng)


