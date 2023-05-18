class InventoryItem:
    def __init__(self, name, price, quantity):
        self.name=name
        self.price= price 
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity):
        item = InventoryItem(name, price, quantity)
        self.items.append(item)
        return 'Item added successfully'

    def sell_item(self, name, quantity):
        item = next((item for item in self.items if item.name == name), None)
        if item is None:
          return 'Item not found'
        elif item.quantity < quantity:
            return'Not enough quantity in stock'
        else:
            total_price = item.price * quantity
            item.quantity -= quantity
            f'{quantity} {name} sold for {total_price}'

inventory = Inventory()


