class Vehicle(object):
    licence_num = None
    size = None

    def __init__(self, licence_num, size):
        self.licence_num = licence_num
        self.size = size

# v = Vehicle("lic")
#
# print v
# print v.licence_num
