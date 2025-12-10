import os
import json
import time
import sys
from .product_service import ProductService

KOK = "\033[34m"
QIZIL = "\033[31m"
YASHIL = "\033[32m"
SARIQ = "\033[33m" 
RANG = "\033[0m"

service = ProductService()

def get_warehouses():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    wh_path = os.path.join(base_dir, "..", "alisher", "data", "warehouses.json")
    if not os.path.exists(wh_path): return []
    try:
        with open(wh_path, "r") as f: return json.load(f)
    except: return []

def get_admins_from_superuser():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    admins_path = os.path.join(base_dir, "..", "alisher", "data", "admins.json")
    if not os.path.exists(admins_path): return []
    try: 
        with open(admins_path, "r") as f: return json.load(f)
    except: return []

def login():
    print(f"{KOK}=== ADMIN TIZIMI ==={RANG}")
    username = input("Username: ")
    password = input("Password: ")
    admins = get_admins_from_superuser()
    for user in admins:
        if user["username"] == username and user["password"] == password:
            return user["username"]
    return None

def admin_menu(user_name):
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"{KOK}=== Admin Panel: {user_name} ==={RANG}")
        print("1. Mahsulot qo'shish")
        print("2. Mahsulot o'chirish")
        print("3. Hisobot (Report) va Ogohlantirish")
        print("4. Tahrirlash (Update)")
        print("5. Qidiruv (Search)")
        print("6. Transfer")
        print(f"{SARIQ}7. Tarix (History){RANG}") 
        print("0. Chiqish")
        
        choice = input(f"{YASHIL}Tanlang: {RANG}")
        
        if choice == "1":
            warehouses = get_warehouses()
            if not warehouses:
                print(f"{QIZIL}Ombor yo'q!{RANG}")
                input("Enter...")
                continue
            name = input("Nomi: ")
            price = input("Narxi: ")
            qty = input("Soni: ")
            if price.isdigit() and qty.isdigit():
                print("Omborlar:")
                for w in warehouses: print(f"ID: {w['id']} | {w['name']}")
                w_id = input("Ombor ID: ")
                service.add_product(name, int(price), int(qty), int(w_id), user_name)
                print(f"{YASHIL}Bajarildi!{RANG}")
            input("Enter...")
            
        elif choice == "2":
            pid = input("ID: ")
            if pid.isdigit() and service.delete_product(int(pid), user_name):
                print(f"{YASHIL}O'chirildi!{RANG}")
            else: print(f"{QIZIL}Xato!{RANG}")
            input("Enter...")
            
        elif choice == "3":
            products = service.get_all()
            print(f"\n{KOK}=== BARCHA MAHSULOTLAR ==={RANG}")
            header = f"{'ID':<4} | {'NOM':<20} | {'NARX ($)':>10} | {'SONI':>8} | {'OMBOR ID':^10}"
            print("-" * len(header))
            print(header)
            print("-" * len(header))
            
            for p in products:
                w_id = str(p.get('warehouse_id', '-'))
                count = p['qty']
                color = QIZIL if count < 5 else RANG
                
                row = f"{p['id']:<4} | {p['name']:<20} | {p['price']:>10} | {count:>8} | {w_id:^10}"
                print(color + row + RANG)
                
            print("-" * len(header))
            print(f"Jami: {len(products)} xil mahsulot")
            input("\nDavom etish uchun Enter...")

        elif choice == "4":
            pid = input("ID: ")
            if pid.isdigit():
                name = input("Yangi nom (Enter=skip): ")
                price = input("Yangi narx: ")
                qty = input("Yangi son: ")
                n = name if name else None
                p = int(price) if price.isdigit() else None
                q = int(qty) if qty.isdigit() else None
                
                if service.update_product(int(pid), user_name, n, p, q):
                    print(f"{YASHIL}Yangilandi!{RANG}")
            input("Enter...")

        elif choice == "5":
            query = input("Qidiruv so'zini kiriting: ")
            loading_animation("Qidirilmoqda") 
            results = service.search_products(query)
            if results:
                print(f"\n{KOK}=== QIDIRUV NATIJALARI ==={RANG}")
                header = f"{'ID':<4} | {'NOM':<20} | {'NARX ($)':>10} | {'SONI':>8} | {'OMBOR ID':^10}"
                print("-" * len(header))
                print(header)
                print("-" * len(header))
                
                for p in results:
                    w_id = str(p.get('warehouse_id', '-'))
                    count = p['qty']
                    color = QIZIL if count < 5 else RANG
                    row = f"{p['id']:<4} | {p['name']:<20} | {p['price']:>10} | {count:>8} | {w_id:^10}"
                    print(color + row + RANG)
                
                print("-" * len(header))
            else:
                print(f"{QIZIL}Afsuski, hech narsa topilmadi.{RANG}")
            
            input("\nDavom etish uchun Enter...")
            
        elif choice == "6":
            pid = input("Tovar ID: ")
            tid = input("Qaysi omborga (ID): ")
            qty = input("Nechta: ")
            if pid.isdigit() and tid.isdigit() and qty.isdigit():
                loading_animation("O'tkazma amalga oshirilmoqda")
                res = service.transfer_product(int(pid), int(tid), int(qty), user_name)
                print(res)
            input("Enter...")
            
        elif choice == "7":
            history = service.get_history()
            print(f"\n{SARIQ}=== TIZIM TARIXI ==={RANG}")
            for h in reversed(history):
                print(f"[{h['time']}] {h['user']} -> {h['action']}: {h['details']}")
            input("\nDavom etish uchun Enter...")

        elif choice == "0":
            break
def loading_animation(text="Bajarilmoqda"):
    """Oddiy nuqtali animatsiya"""
    print(f"{YASHIL}{text}", end="")
    for _ in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.4) 
    print(f"{RANG}")

def admin_panel():
    os.system("cls" if os.name == "nt" else "clear")
    user = login()
    if user: admin_menu(user)
    else: input(f"{QIZIL}Xato!{RANG}")