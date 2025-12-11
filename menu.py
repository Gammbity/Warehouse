import os
from dastur_kodlari.Shahzoda.admin import admin_menu as admin_panel
from dastur_kodlari.alisher.superuser_service import run_superuser_system
KOK   = "\033[34m"
QIZIL = "\033[31m"
YASHIL = "\033[32m"
SARIQ = "\033[33m"
RANG  = "\033[0m"


def warehouse_menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(KOK + r"""
 _       __  ___    ____    ______   __  __   ____    __  __   _____    ______
| |     / / /   |  / __ \  / ____/  / / / /  / __ \  / / / /  / ___/   / ____/
| | /| / / / /| | / /_/ / / __/    / /_/ /  / / / / / / / /   \__ \   / __/   
| |/ |/ / / ___ |/ _, _/ / /___   / __  /  / /_/ / / /_/ /   ___/ /  / /___   
|__/|__/ /_/  |_/_/ |_| /_____/  /_/ /_/   \____/  \____/   /____/  /_____/   
        """ + RANG)
        
        print(f"{YASHIL}=== TIZIM BOSHQARUVI ==={RANG}")
        print(f"1. {KOK}Admin Panel{RANG}")
        print(f"2. {SARIQ}SuperUser Panel{RANG}")
        print(f"0. {QIZIL}Chiqish{RANG}")
        
        tanlov = input(f"\n{YASHIL}>>> Tanlovni kiriting: {RANG}")
        
        if tanlov == "1":
            admin_panel()
        elif tanlov == "2":
            run_superuser_system()
        elif tanlov == "0":
            print("Xayr, salomat bo'ling!")
            break
        else:
            print(f"{QIZIL}Noto'g'ri tanlov!!!{RANG}")
            input("Enter...")


if __name__ == "__main__":
    warehouse_menu()

