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
    for i in adminlar:
        login = input("Loginni kiriting: ")
        parol = input("Parolni kiriting: ")
        if i["login"] == login and i["parol"] == parol:
            print("Siz tizimga muvafaqiyatli kirdingiz.")
        else:
            print("Login yoki parol xato!!!")
            return
        while True:
           pass
        

