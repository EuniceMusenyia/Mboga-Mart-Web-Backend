class Order:
    def __init__(self, customer_name, customer_email, items):
        self.customer_name=customer_name,
        self.customer_email=customer_email
        self.items = items

    def calculate_total(self):
        return sum(item.price * item.quantity for item in self.items)

orders = []

def create_order():
    customer_name = input('Customer name: ')
    customer_email = input('Customer email: ')
    items = []
    while True:
        name = input('Item name (0 to finish): ')
        if name == '0':
            break
        item = next((item for item in inventory.items if item.name == name), None)
        if item is None:
            return'Item not found'
        else:
            quantity = int(input('Quantity: '))
            if item.quantity < quantity:
               return'Not enough quantity in stock'
            else:
                items.append(item)
                item.quantity -= quantity
                return (f'{quantity} {name} added to order')
    if not items:
       return'No items added to order'
    else:
        order = Order(customer_name, customer_email, items)
        orders.append(order)
    return f'Order created successfully with total amount of {order.calculate_total()}'
