import os
import json
from .product_service import ProductService

# Цвета для консоли
KOK = "\033[34m"
QIZIL = "\033[31m"
YASHIL = "\033[32m"
RANG = "\033[0m"

# Инициализируем сервис товаров
service = ProductService()

def get_admins_from_superuser():
    """
    Читает список админов из файла, который создает модуль Alisher (SuperUser).
    """
    # Вычисляем путь к файлу admins.json относительно текущего файла
    base_dir = os.path.dirname(os.path.abspath(__file__)) # папка shaxnoza
    # Поднимаемся на уровень выше и заходим в alisher/data/admins.json
    admins_path = os.path.join(base_dir, "..", "alisher", "data", "admins.json")
    
    if not os.path.exists(admins_path):
        return []
    
    try:
        with open(admins_path, "r") as f:
            return json.load(f)
    except:
        return []

def login():
    """Функция авторизации админа"""
    print(f"{KOK}=== ADMIN TIZIMI ==={RANG}")
    username = input("Username: ")
    password = input("Password: ")
    
    admins = get_admins_from_superuser()
    
    for user in admins:
        # Проверяем совпадение логина и пароля
        # Допускаем вход, если роль 'admin' или 'superuser'
        if user["username"] == username and user["password"] == password:
            return user["username"]
    
    return None

def admin_menu(user_name):
    """Главное меню админа после входа"""
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"{KOK}=== Admin Panel: {user_name} ==={RANG}")
        print("1. Mahsulot qo'shish (Add Product)")
        print("2. Mahsulot o'chirish (Delete Product)")
        print("3. Mahsulotlarni ko'rish (Report)")
        print("0. Chiqish (Exit)")
        
        choice = input(f"{YASHIL}Tanlang: {RANG}")
        
        if choice == "1":
            name = input("Mahsulot nomi: ")
            price = input("Narxi: ")
            qty = input("Soni: ")
            if price.isdigit() and qty.isdigit():
                service.add_product(name, int(price), int(qty))
                print(f"{YASHIL}Qo'shildi!{RANG}")
            else:
                print(f"{QIZIL}Narx va son raqam bo'lishi kerak!{RANG}")
            input("Davom etish uchun Enter...")
            
        elif choice == "2":
            pid = input("O'chiriladigan ID: ")
            if pid.isdigit():
                if service.delete_product(int(pid)):
                    print(f"{YASHIL}O'chirildi!{RANG}")
                else:
                    print(f"{QIZIL}ID topilmadi!{RANG}")
            else:
                print(f"{QIZIL}ID raqam bo'lishi kerak!{RANG}")
            input("Davom etish uchun Enter...")
            
        elif choice == "3":
            products = service.get_all()
            print(f"\n{KOK}--- SKLAD ---{RANG}")
            for p in products:
                print(f"ID: {p['id']} | Nomi: {p['name']} | Narx: {p['price']} | Soni: {p['qty']}")
            print(f"Jami mahsulotlar: {len(products)}")
            input("\nDavom etish uchun Enter...")
            
        elif choice == "0":
            break

def admin_panel():
    """Точка входа, вызываемая из menu.py"""
    os.system("cls" if os.name == "nt" else "clear")
    user = login()
    if user:
        print(f"{YASHIL}Xush kelibsiz, {user}!{RANG}")
        input("Kirish uchun Enter...")
        admin_menu(user)
    else:
        print(f"{QIZIL}Login yoki parol xato!{RANG}")
        input("Menyuga qaytish uchun Enter...")