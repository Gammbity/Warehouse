import os
from dastur_kodlari.shaxnoza.admin import admin_panel
from dastur_kodlari.alisher.superuser import super_user
KOK="\033[34m"
QIZIL="\033[31m"
YASHIL="\033[32m"
RANG="\033[0m" 

def warehouse_menu():
    os.system("cls")
    while True:
        print(f"""
         {KOK}Welcome to Warehouse

                1.Admin:
                2.SuperUser:{RANG}
            """)
        tanlov = input(f"{YASHIL}Tanlovni kiriting: {RANG}")
        if tanlov == "1":
            admin_panel()
        elif tanlov == "2":
            super_user()

        else:
            print(f"{QIZIL}Noto'g'ri tanlov!!!{RANG}")
            print(f"{QIZIL}Boshidan tanlang.{RANG}")


if __name__ == "__main__":
    warehouse_menu()
