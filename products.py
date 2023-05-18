class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description
products = []
def add_product():
    name = input("Enter product name: ")
    price = int(input("Enter product price: "))
    description = input("Enter product description: ")
    product = Product(name, price, description)
    products.append(product)
    f" added successfully"