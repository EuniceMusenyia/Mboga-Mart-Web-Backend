class InventoryItem:
    def __init__(self, name, price, quantity):
        self.name=name
        self.price=price
        self.quantity =quantity

inventory_items = []

def add_item():
    item = InventoryItem(input('Name: '), int(input('Price: ')), int(input('Quantity: ')))
    inventory_items.append(item)
    return'Item added successfully'

