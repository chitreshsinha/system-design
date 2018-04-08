class Vehicle(object):
    name = None
    rank = None
    kms_travelled = 0
    lat = None
    lng = None
    type = None
    slot = {}

    def __init__(self, type, name, rank, kms_travelled, lat, lng):
        self.name = name
        self.rank = rank
        self.kms_travelled = kms_travelled
        self.lat = lat
        self.lng = lng
        self.type = type
        self.slot = {}

    def add_slot_price(self, date, from_slot, to_slot, price):
        from_slot = int(from_slot)
        to_slot = int(to_slot)

        for x in range(from_slot, to_slot):
            self.slot[date+"#"+str(x)+"-"+str(x+1)] = {"price": price,
                                                       "booked": False,
                                                       "booked_by": None
                                                       }

    def book(self, date, from_slot, to_slot, user):
        from_slot = int(from_slot)
        to_slot = int(to_slot)

        for x in range(from_slot, to_slot):
            key = date + "#" + str(x) + "-" + str(x+1)
            if not ((key in self.slot) and (self.slot[key]["booked"] == False)):
                return -1, "Slot not available"

        for x in range(from_slot, to_slot):
            key = date+"#"+str(x)+"-"+str(x+1)
            if ((key in self.slot) and (self.slot[key]["booked"] == False)):
                self.slot[key]["booked"] = True
                self.slot[key]["booked_by"] = user

        return 0, "Success"


    def cancel(self, date, from_slot, to_slot, user):
        from_slot = int(from_slot)
        to_slot = int(to_slot)

        for x in range(from_slot, to_slot):
            key = date + "#" + str(x) + "-" + str(x + 1)
            if not ((key in self.slot)
                    and (self.slot[key]["booked"] == True)
                    and (self.slot[key]["booked_by"] == user)):
                return -1, "Can't cancel"

        for x in range(from_slot, to_slot):
            key = date + "#" + str(x) + "-" + str(x + 1)
            if ((key in self.slot)
                    and (self.slot[key]["booked"] == True)
                    and (self.slot[key]["booked_by"] == user)):
                self.slot[key]["booked"] = False
                self.slot[key]["booked_by"] = None

        return 0, "Success"








