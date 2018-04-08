from Vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, licence_num):
        super(Truck, self).__init__(licence_num, 4)
