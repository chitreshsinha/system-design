from Inventory import Inventory
from InternalController import InternalController
from ExternalController import ExternalController
from Car import Car

# inv = Inventory.get_instance()
#
# inv2 = Inventory.get_instance()
#
# print inv, inv2

ic = InternalController()
ec = ExternalController()

#ec.show_available_vehicles()

inv = Inventory.get_instance()

#inv.show_all_vehicles()
#ec.show_available_vehicles()

inv.inventory["Bus3"].add_slot_price("20180404", 0, 24, 2000)

#ec.show_available_vehicles()

inv.inventory["Bus2"].book("20180404", 3, 7, "chitresh")

ec.available_vehicles("20180404", 3, 7, vtype="Bus")

inv.inventory["Bus2"].cancel("20180404", 3, 7, "chitresh")

ec.available_vehicles("20180404", 3, 7, vtype="Bus", sort=True)

c = Car("New Car", 20, 1000, 23.23, 123.123)

print c.name

