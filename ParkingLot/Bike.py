from Vehicle import Vehicle

class Bike(Vehicle):
    def __init__(self, licence_num):
        super(Bike, self).__init__(licence_num, 1)
