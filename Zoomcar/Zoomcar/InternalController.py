from Inventory import Inventory

class InternalController():
    def __init__(self):
        inv = Inventory.get_instance()

        inv.add_to_inventory("Car", "Car1", 5, 0, 0, 1)
        inv.add_to_inventory("Car", "Car2", 8, 0, 2, 3)
        inv.add_to_inventory("Car", "Car3", 3, 0, 4, 5)
        inv.add_to_inventory("Bike", "Bike1", 1, 0, 6, 7)
        inv.add_to_inventory("Bike", "Bike2", 4, 0, 8, 9)
        inv.add_to_inventory("Bike", "Bike3", 9, 0, 10, 11)
        inv.add_to_inventory("Bus", "Bus1", 5, 0, 12, 13)
        inv.add_to_inventory("Bus", "Bus2", 7, 0, 14, 15)
        inv.add_to_inventory("Bus", "Bus3", 6, 0, 16, 17)

        price = 1000

        for x in inv.inventory:
            v = inv.inventory[x]

            v.add_slot_price("20180404", 0, 24, price)

            price += 100

        print inv.inventory
