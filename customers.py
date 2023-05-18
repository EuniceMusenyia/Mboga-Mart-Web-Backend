#Customer class
class Customer:
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number
customers = []
def add_customer():
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    phone_number = input("Enter customer phone number: ")
    customer = Customer(name, email, phone_number)
    customers.append(customer)
    return f"Customer added successfully"