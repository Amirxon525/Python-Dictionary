from time import sleep
from termcolor import colored


def print_menu() -> None:
    print("========== Menu ==========")
    print("1: Kontakt qo'shish (ism → telefon)")
    print("2: Barcha kontaktlarni chiqarish")
    print("3: Ism bo'yicha telefon qidirish")
    print("4: Dasturdan chiqish")

def add_contact(phonebook: dict[str, str]) -> None:
    print("Contact malumotlarini kiriting")
    name = input("Name: ").strip().title()
    phone = input("Phone: ")

    if name in phonebook.keys() or not phone.isdigit():
        print(colored("xatolik yuz berdi.","red"))
        return
    phonebook[name] = phone
    print(colored("qoshildi", "green"))

def show_contact(phonebook: dict[str, str]) -> None:
    if not phonebook:
        print(colored("contact mavjud emas", "red"))
        return
    
    print("Barcha contactlar")
    for number, contact in enumerate(phonebook, start=1):
        print(f"{number}. {contact} → {phonebook[contact]}")

def phonebook_menu(phonebook: dict[str, str]) -> None:
    while True:
        print_menu()

        choice = input(colored("Menu Tanlang: ", "blue"))
        if choice == '1':
            add_contact(phonebook)
        elif choice == '2':
            show_contact(phonebook)
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        else:
            print(colored("Bundan menu mavjud emas.", "red"))

        print(colored("\n------------------------------\n", "blue"))
        
        sleep(2)


phonebook = dict()
phonebook_menu(phonebook)