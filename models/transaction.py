class Transaction:

    def __init__(self, merchant, amount, date, tag, id = None):
        self.merchant = merchant
        self.amount = amount
        self.date = date
        self.tag = tag
        self.id = id