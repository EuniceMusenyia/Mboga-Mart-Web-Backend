class Products:
    def __init__(self,id,name,price):
        self.id=id
        self.name=name
        self.price=price
class Cart:
    def __init__(self):
        self.item=[]
    def add_item(self,item):
        #check if if item is in the cart
        for i in self.item:
            if i.product.id == item.product.id:
                # increase the item quantity
                i.quantity +=item.quantity
                break;
        else:
            #add item to the cart
            self.item.append(item)
            def remove_item(self,product_id):
                self.product_id=product_id
                for i in self.items:
                    if i.product.id ==product_id:
                            self.item.remove(i)
                            break
    def total(self):
        #get the total cost
        total=0
        for i in self.item:
            total +=i.product.price *i.quantity
        return total
class Cart_to_item:
    def __init__(self,product,quantity):
        self.product=product
        self.quantity=quantity
        # return cart.total
cart=Cart()
product=Products(2,'cabbage',50)
item=Cart_to_item(product,1)
cart.add_item(item)