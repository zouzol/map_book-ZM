from utils.controller import get_user_info, add_user
from utils.model import users

def main():
    while True:
        print("=============MENU=============")
        print("0 - zamknij aplikację")
        print("1 - wyświetl co u znajomych")
        print("2 - dodaj nowego użytkownika")
        print("3 - usuń nowego użytkownika")
        print("4 - edytuj użytkownika")
        print("=============MENU=============")

        choice = input("Wybierz opcję menu ")
        if choice == "0": break
        if choice == "1": get_user_info(users)
        if choice == "2": add_user(users)


if __name__ == "__main__":
    main()




