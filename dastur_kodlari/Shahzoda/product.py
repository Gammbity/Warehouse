class Product:
    def __init__(self, pid, name, qty, price):
        self.id = pid
        self.name = name
        self.qty = qty
        self.price = price

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "qty": self.qty,
            "price": self.price
        }
