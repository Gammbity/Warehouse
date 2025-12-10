import json
import os
from datetime import datetime

class ProductService:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.data_dir = os.path.join(base_dir, "data")
        self.file_path = os.path.join(self.data_dir, "products.json")
        self.history_path = os.path.join(self.data_dir, "history.json") 
        
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        if not os.path.exists(self.file_path):
            self._save([])
        if not os.path.exists(self.history_path):
            self._save_history([])

    def _load(self):
        try:
            with open(self.file_path, "r") as f: return json.load(f)
        except: return []

    def _save(self, data):
        with open(self.file_path, "w") as f: json.dump(data, f, indent=4)

    def _load_history(self):
        try:
            with open(self.history_path, "r") as f: return json.load(f)
        except: return []

    def _save_history(self, data):
        with open(self.history_path, "w") as f: json.dump(data, f, indent=4)
        
    def log_action(self, user, action, details):
        history = self._load_history()
        record = {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "user": user,
            "action": action,
            "details": details
        }
        history.append(record)
        self._save_history(history)

    def get_history(self):
        return self._load_history()

    def get_all(self):
        return self._load()

    def add_product(self, name, price, qty, warehouse_id, user):
        products = self._load()
        new_id = 1
        if products: new_id = products[-1]["id"] + 1
            
        new_product = {
            "id": new_id, "name": name, "price": price, 
            "qty": qty, "warehouse_id": warehouse_id
        }
        products.append(new_product)
        self._save(products)
        self.log_action(user, "Add", f"{name} ({qty} ta) -> Ombor {warehouse_id}")
        return True

    def delete_product(self, pid, user):
        products = self._load()
        initial_len = len(products)
        deleted_item = next((p for p in products if p["id"] == pid), None)
        products = [p for p in products if p["id"] != pid]
        
        if len(products) < initial_len:
            self._save(products)
            item_name = deleted_item['name'] if deleted_item else 'Unknown'
            self.log_action(user, "Delete", f"ID: {pid} | {item_name}")
            return True
        return False

    def update_product(self, pid, user, name=None, price=None, qty=None):
        products = self._load()
        updated = False
        for p in products:
            if p["id"] == pid:
                changes = []
                if name: 
                    changes.append(f"Name: {p['name']}->{name}")
                    p["name"] = name
                if price is not None: 
                    changes.append(f"Price: {p['price']}->{price}")
                    p["price"] = price
                if qty is not None: 
                    changes.append(f"Qty: {p['qty']}->{qty}")
                    p["qty"] = qty
                
                if changes:
                    updated = True
                    self.log_action(user, "Update", f"ID: {pid} | " + ", ".join(changes))
                break
        
        if updated:
            self._save(products)
            return True
        return False

    def search_products(self, query):
        products = self._load()
        result = []
        query = query.lower()
        for p in products:
            if query in p["name"].lower(): result.append(p)
        return result

    def transfer_product(self, product_id, target_warehouse_id, qty, user):
        products = self._load()
        source_product = None
        for p in products:
            if p["id"] == product_id:
                source_product = p
                break
        
        if not source_product: return "Mahsulot topilmadi"
        if source_product["qty"] < qty: return "Yetarli emas"
        if source_product.get("warehouse_id") == target_warehouse_id: return "Ayni omborda"

        source_product["qty"] -= qty
        p_name = source_product["name"]
        from_wh = source_product.get("warehouse_id")

        dest_product = None
        for p in products:
            p_wh = p.get("warehouse_id")
            if (p["name"] == source_product["name"] and 
                p["price"] == source_product["price"] and 
                p_wh == target_warehouse_id):
                dest_product = p
                break
        
        if dest_product:
            dest_product["qty"] += qty
        else:
            new_id = products[-1]["id"] + 1 if products else 1
            new_p = {
                "id": new_id, "name": source_product["name"],
                "price": source_product["price"], "qty": qty,
                "warehouse_id": target_warehouse_id
            }
            products.append(new_p)

        self._save(products)
        self.log_action(user, "Transfer", f"{p_name} ({qty} ta) | Ombor {from_wh} -> {target_warehouse_id}")
        return "Success"