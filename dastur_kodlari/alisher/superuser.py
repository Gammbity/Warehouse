from dastur_kodlari.alisher.utils import load, save, ensure_json, color

ADMINS = "dastur_kodlari/alisher/data/admins.json"
WAREHOUSES = "dastur_kodlari/alisher/data/warehouses.json"

def init_files():
    ensure_json(ADMINS, [
        {"username": "root", "password": "123", "role": "superuser"}
    ])
    ensure_json(WAREHOUSES, [])

def view_admins():
    admins = load(ADMINS)
    print(color("\n=== ADMINLAR RO‘YXATI ===", "cyan"))
    for a in admins:
        print(f"Username: {a['username']} | Role: {a['role']}")
    print()

def create_admin():
    admins = load(ADMINS)
    u = input("Yangi admin username: ")
    p = input("Parol: ")
    admins.append({"username": u, "password": p, "role": "admin"})
    save(ADMINS, admins)
    print(color("Admin qo‘shildi.\n", "green"))

def delete_admin():
    admins = load(ADMINS)
    u = input("O'chiriladigan username: ")
    admins = [x for x in admins if x["username"] != u]
    save(ADMINS, admins)
    print(color("Admin o'chirildi.\n", "red"))

def update_admin():
    admins = load(ADMINS)
    u = input("O'zgartiriladigan username: ")
    for a in admins:
        if a["username"] == u:
            a["password"] = input("Yangi parol: ")
            save(ADMINS, admins)
            print(color("Admin yangilandi.\n", "yellow"))
            return
    print(color("Admin topilmadi.\n", "red"))

def view_warehouses():
    ws = load(WAREHOUSES)
    print(color("\n=== OMBORLAR RO'YXATI ===", "cyan"))
    for w in ws:
        print(f"ID: {w['id']} | Name: {w['name']}")
    print()

def create_warehouse():
    ws = load(WAREHOUSES)
    name = input("Ombor nomi: ")
    new_id = 1 if not ws else ws[-1]["id"] + 1
    ws.append({"id": new_id, "name": name})
    save(WAREHOUSES, ws)
    print(color("Ombor yaratildi.\n", "green"))

def delete_warehouse():
    ws = load(WAREHOUSES)
    wid = int(input("O'chiriladigan ombor ID: "))
    ws = [x for x in ws if x["id"] != wid]
    save(WAREHOUSES, ws)
    print(color("Ombor o'chirildi.\n", "red"))

def report():
    admins = load(ADMINS)
    ws = load(WAREHOUSES)
    print(color("\n=== HISOBOT ===", "blue"))
    print("Adminlar soni:", len(admins))
    print("Omborlar soni:", len(ws))
    print()
