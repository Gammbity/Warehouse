import os


KOK = "\033[34m"
QIZIL = "\033[31m"
YASHIL = "\033[32m"
RANG = "\033[0m"

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
        
        topildi = False

        for admin in adminlar:
            os.system("cls")
            if admin["login"] == login and admin["parol"] == parol:
                topildi = True
                print("Siz tizimga muvafaqiyatli kirdingiz.")
                while True:
                    pass   
                
        if topildi == False:
            os.system("cls")
            urinish += 1
            print(f"{QIZIL}Login yoki parol xato!!!{RANG}")
            
            if urinish < 2:
                print("Login va parolni qayta kiriting.")

    print("Urinishlar soni ikki martadan oshib ketti!!!")
    return
