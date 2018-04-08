from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, licence_num):
        super(Car, self).__init__(licence_num, 2)


# c = Car("ABC")
#
# print c
# print c.licence_num

# c = Vehicle("test")
# print c
# print c.licence_num
