KOK="\033[34m"
QIZIL="\033[31m"
YASHIL="\033[32m"
RANG="\033[0m" 


def admin_panel():
    login = "admin"
    parol = "1234"

    l = input(f"{YASHIL}Loginni kiriting: {RANG}")
    p = int(input(f"{YASHIL}Parolni kiriting: {RANG}"))

    if login != l or parol == p:
            print(f"{QIZIL}Login xato!!!{RANG}")
            print(f"{QIZIL}Iltimos login va parol qayta kiriting {RANG}")
            return admin_panel()
    while True:
          pass