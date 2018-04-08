from Car import Car
from Bike import Bike
from Bus import Bus

class Inventory(object):
    inventory = {}

    __instance = None

    def __init__(self):
        #print 1
        if Inventory.__instance is not None:
            #print 2
            raise Exception("An instantiation already exists!")
        else:
            #print 3
            Inventory.__instance = self
            self.inventory = {}

    @staticmethod
    def get_instance():
        if Inventory.__instance is None:
            Inventory()
        return Inventory.__instance

    def add_to_inventory(self, type, name, rank, kms_travelled, lat, lng):
        #v = Vehicle(type, name, rank, kms_travelled, lat, lng)
        if type == "Car":
            v = Car(name, rank, kms_travelled, lat, lng)
        elif type == "Bike":
            v = Bike(name, rank, kms_travelled, lat, lng)
        elif type == "Bus":
            v = Bus(name, rank, kms_travelled, lat, lng)
        else:
            raise Exception("Invalid vehicle type")

        self.inventory[v.name] = v

    def show_all_vehicles(self):
        print "--------"
        print "Showing all available vehicles"
        for x in self.inventory:
            v = self.inventory[x]
            print "--------"
            print v.name, v.type, v.rank
            for s in self.inventory[x].slot:
                print s, self.inventory[x].slot[s]


#inv = Inventory()








