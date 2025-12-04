import os

KOK="\033[34m"
QIZIL="\033[31m"
YASHIL="\033[32m"
RANG="\033[0m" 




def super_user():
    os.system("cls")
    login = "superuser"
    parol = "1234"
    urinish = 0

    while urinish < 2:
        l = input(f"{YASHIL}Loginni kiriting: {RANG}")
        p = input(f"{YASHIL}Parolni kiriting: {RANG}")

        if l == login and p == parol:
            os.system("cls")
            print("Muvaffaqiyatli kirdingiz!")
            while True:
                pass
        
        
        urinish += 1

        if urinish < 2:
            os.system("cls")
            print(f"{QIZIL}Login yoki parol xato!!!{RANG}")
            print("Login va parolni qayta kiriting.")

    os.system("cls")
    print(f"{QIZIL}Urinishlar soni ikkitadan ortib ketdi!!!{RANG}")
    return  
