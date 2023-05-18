class Payment:
    def __init__(self, amount, payment_method):
        self.amount = amount
        self.payment_method = payment_method
payments = []
def add_payment():
    amount = int(input("Enter payment amount: "))
    payment_method = input("Enter payment method: ")
    payment = Payment(amount, payment_method)
    payments.append(payment)
    return"Payment added successfully"