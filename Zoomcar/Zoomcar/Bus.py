from Vehicle import Vehicle

class Bus(Vehicle):

    def __init__(self, name, rank, kms_travelled, lat, lng):
        super(Bus, self).__init__("Bus", name, rank, kms_travelled, lat, lng)


