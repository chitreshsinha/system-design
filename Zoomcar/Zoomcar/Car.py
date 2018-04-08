from Vehicle import Vehicle

class Car(Vehicle):

    def __init__(self, name, rank, kms_travelled, lat, lng):
        super(Car, self).__init__("Car", name, rank, kms_travelled, lat, lng)


