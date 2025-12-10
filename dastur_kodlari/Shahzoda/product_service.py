from .storage import load, save
from .product import Product


class ProductService:
    filename = "products.json"

    def get_all(self):
        return load(self.filename)

    def add(self, name, qty, price):
        items = self.get_all()
        new_id = len(items) + 1

        p = Product(new_id, name, qty, price)
        items.append(p.to_dict())
        save(self.filename, items)

    def delete(self, pid):
        items = self.get_all()
        updated = [i for i in items if i["id"] != pid]

        if len(updated) == len(items):
            return False

        save(self.filename, updated)
        return True

    def update(self, pid, name=None, qty=None, price=None):
        items = self.get_all()

        for item in items:
            if item["id"] == pid:
                if name:
                    item["name"] = name
                if qty:
                    item["qty"] = qty
                if price:
                    item["price"] = price

                save(self.filename, items)
                return True

        return False
