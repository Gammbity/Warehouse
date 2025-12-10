import os
import platform
from dastur_kodlari.Shahzoda.admin import admin_panel
from dastur_kodlari.alisher.superuser_service import run_superuser_system

KOK = "\033[34m"
QIZIL = "\033[31m"
YASHIL = "\033[32m"
RANG = "\033[0m"


def clear_screen():
    if "TERM" not in os.environ:
        os.environ["TERM"] = "xterm"
    if platform.system() == "Windows":
        os.system("cls")
    else:
        try:
            os.system("clear")
        except Exception:
            print("\n" * 100)


KOK = "\033[34m"
QIZIL = "\033[31m"
YASHIL = "\033[32m"
RANG = "\033[0m"


def warehouse_menu():
    os.system("cls")
    while True:
        clear_screen()
        print(f"""
         {KOK}Welcome to Warehouse

                1. Admin
                2. SuperUser{RANG}
        """)
        tanlov = input(f"{YASHIL}Tanlovni kiriting: {RANG}")
        if tanlov == "1":
            admin_panel()
        elif tanlov == "2":
            run_superuser_system()
            super_user()

        else:
            print(f"{QIZIL}Noto'g'ri tanlov!!!{RANG}")
            input(f"{QIZIL}Boshidan tanlang. Enter bosish orqali davom eting.{RANG}")


if __name__ == "__main__":
    warehouse_menu()
