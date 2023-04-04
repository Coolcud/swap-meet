class Vendor:
    def __init__(self, inventory=None):
        if not inventory:
            inventory = []
        self.inventory = inventory
    
    def add(self, item):
        if item:
            self.inventory.append(item)
        
        return item

    def remove(self, item):
        try:
            self.inventory.remove(item)
            return item
        except ValueError as err:
            print(f"Error message: {err}")
            print(f"Unable to remove '{item}' from inventory.")
            return False
    
    def get_by_id(self, id):
        try:
            for item in self.inventory:
                if item.id == id:
                    return item
        except ValueError as err:
            print(f"Error message: {err}")
            print(f"Could not retrieve item {id} from inventory.")
            return None
        
    def swap_items(self, other_vendor, my_item, their_item):
        if (my_item not in self.inventory or
                their_item not in other_vendor.inventory):
            return False

        self.inventory.remove(my_item)
        other_vendor.inventory.append(my_item)
        other_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)
        
        return True