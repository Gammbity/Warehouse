from dastur_kodlari.alisher.utils import load, color
from dastur_kodlari.alisher.superuser import (
    init_files, view_admins, create_admin, delete_admin, update_admin,
    view_warehouses, create_warehouse, delete_warehouse, report
)

def login():
    users = load("dastur_kodlari/alisher/data/admins.json")
    u = input("Username: ")
    p = input("Password: ")
    for usr in users:
        if usr["username"] == u and usr["password"] == p:
            return usr["role"]
    return None

def superuser_menu():
    while True:
        print(color("\n=== SUPERUSER MENU ===", "blue"))
        print("1. Adminlar ro'yxati")
        print("2. Create Admin")
        print("3. Delete Admin")
        print("4. Update Admin")
        print("5. Omborlar ro'yxati")
        print("6. Create Warehouse")
        print("7. Delete Warehouse")
        print("8. Report")
        print("0. Chiqish")

        c = input("Tanlang: ")

        if c == "1": view_admins()
        elif c == "2": create_admin()
        elif c == "3": delete_admin()
        elif c == "4": update_admin()
        elif c == "5": view_warehouses()
        elif c == "6": create_warehouse()
        elif c == "7": delete_warehouse()
        elif c == "8": report()
        elif c == "0": break


def run_superuser_system():
    init_files()
    role = login()
    if role == "superuser":
        superuser_menu()
    else:
        print(color("Kirish rad etildi.", "red"))
        input("Menyuga qaytish uchun Enterni bosing...")