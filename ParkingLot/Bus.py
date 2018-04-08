from Vehicle import Vehicle

class Bus(Vehicle):
    def __init__(self, licence_num):
        super(Bus, self).__init__(licence_num, 3)
        
