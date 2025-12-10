import os
from .product_service import ProductService

KOK = "\033[34m"
QIZIL = "\033[31m"
YASHIL = "\033[32m"
RANG = "\033[0m"

product_service = ProductService()

adminlar = [
    {
        "id": 1,
        "login": "admin1",
        "parol": "password123",
        "ism": "Ali"
    },
    {
        "id": 2,
        "login": "admin2",
        "parol": "adminpass456",
        "ism": "Bekzod"
    },
    {
        "id": 3,
        "login": "admin3",
        "parol": "secure789",
        "ism": "Javohir"
    }
]


def admin_panel():
    os.system("cls")
    urinish = 0

    while urinish < 2:
        login = input(f"{YASHIL}Loginni kiriting: {RANG}")
        parol = input(f"{YASHIL}Parolni kiriting: {RANG}")

        for admin in adminlar:
            if admin["login"] == login and admin["parol"] == parol:
                os.system("cls")
                print(f"{YASHIL}Tizimga muvaffaqiyatli kirdingiz, {admin['ism']}!{RANG}")

                # 🔥 BU YERDA ADMIN MENU CHAQIRILADI
                admin_menu(admin["ism"])
                return

        # agar admin topilmasa
        urinish += 1
        os.system("cls")
        print(f"{QIZIL}Login yoki parol xato!!!{RANG}")
        if urinish < 2:
            print("Qayta urinib ko‘ring.")

    print(f"{QIZIL}Urinishlar soni 2 martadan oshdi. Kirish bloklandi.{RANG}")
    return


def admin_menu(admin_name):
    while True:
        os.system("cls")
        print(f"{KOK}=== Admin panel — {admin_name} ==={RANG}")
        print("1. Add product")
        print("2. Delete product")
        print("3. Update product")
        print("4. Report")
        print("0. Exit")

        choice = input("Tanlov: ")

        # ADD
        if choice == "1":
            name = input("Product name: ")
            qty = int(input("Quantity: "))
            price = float(input("Price: "))

            product_service.add(name, qty, price)
            print(f"{YASHIL}Product added!{RANG}")
            input("Enter...")

        # DELETE
        elif choice == "2":
            pid = int(input("Product ID: "))
            if product_service.delete(pid):
                print(f"{YASHIL}Deleted!{RANG}")
            else:
                print(f"{QIZIL}Product not found{RANG}")
            input("Enter...")

        # UPDATE
        elif choice == "3":
            pid = int(input("Product ID: "))

            new_name = input("New name (empty=skip): ")
            new_qty = input("New quantity: ")
            new_price = input("New price: ")

            new_name = new_name if new_name else None
            new_qty = int(new_qty) if new_qty else None
            new_price = float(new_price) if new_price else None

            if product_service.update(pid, new_name, new_qty, new_price):
                print(f"{YASHIL}Updated!{RANG}")
            else:
                print(f"{QIZIL}Product not found{RANG}")
            input("Enter...")

        # REPORT
        elif choice == "4":
            items = product_service.get_all()

            print("\n=== REPORT ===")
            for i in items:
                print(f"{i['id']}. {i['name']} | {i['qty']} pcs | ${i['price']}")
            input("Enter...")

        # EXIT
        elif choice == "0":
            print("Chiqildi.")
            break

        else:
            print(f"{QIZIL}Noto‘g‘ri tanlov!{RANG}")
            input("Enter...")

