import json
import os

class ProductService:
    def __init__(self):
        # Определяем путь к файлу products.json внутри папки shaxnoza/data
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.data_dir = os.path.join(base_dir, "data")
        self.file_path = os.path.join(self.data_dir, "products.json")
        
        # Создаем папку data, если её нет
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
            
        # Создаем пустой файл, если его нет
        if not os.path.exists(self.file_path):
            self._save([])

    def _load(self):
        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
        except:
            return []

    def _save(self, data):
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)

    def get_all(self):
        return self._load()

    def add_product(self, name, price, qty):
        products = self._load()
        # Генерируем новый ID
        new_id = 1
        if products:
            new_id = products[-1]["id"] + 1
            
        new_product = {
            "id": new_id,
            "name": name,
            "price": price,
            "qty": qty
        }
        products.append(new_product)
        self._save(products)

    def delete_product(self, pid):
        products = self._load()
        initial_len = len(products)
        # Оставляем только те товары, у которых ID не совпадает с удаляемым
        products = [p for p in products if p["id"] != pid]
        
        if len(products) < initial_len:
            self._save(products)
            return True
        return False