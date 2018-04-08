from Inventory import Inventory

class ExternalController():
    def __init__(self):
        pass

    def show_available_vehicles(self):
        inv = Inventory.get_instance()
        inv.show_all_vehicles()

    def print_available_vehicles(self, veh_list):
        for v in veh_list:
            for key in v[6]:
                print v[0], v[1], v[2], v[3], v[4], v[5], key, v[6][key]

    def available_vehicles(self, date, from_slot, to_slot, vtype=None, sort=False):
        print "======================================"
        print "Showing available vehicles"
        print "======================================"
        result = []
        inv = Inventory.get_instance()

        from_slot = int(from_slot)
        to_slot = int(to_slot)

        filtered_inventory1 = {}
        filtered_inventory2 = {}

        if vtype:
            for key in inv.inventory:
                if inv.inventory[key].type == vtype:
                    filtered_inventory1[key] = inv.inventory[key]
        else:
            filtered_inventory1 = inv.inventory

        for key in filtered_inventory1:
            flag = True
            veh_slot = {}

            for x in range(from_slot, to_slot):
                datekey = date + "#" + str(x) + "-" + str(x + 1)
                slots = filtered_inventory1[key].slot
                if not ((datekey in slots) and (slots[datekey]["booked"] == False)):
                    flag = False
                    break
                else:
                    veh_slot[datekey] = slots[datekey]

            if (flag):
                filtered_inventory2[key] = filtered_inventory1[key]
                filtered_inventory2[key].slot = veh_slot

        for key in filtered_inventory2:
            vehicle = filtered_inventory2[key]
            result.append([vehicle.name, vehicle.type, vehicle.rank,
                           vehicle.kms_travelled, vehicle.lat,
                           vehicle.lng, vehicle.slot])

        if (sort):
            result = sorted(result, key=lambda x: x[6])

        self.print_available_vehicles(result)


