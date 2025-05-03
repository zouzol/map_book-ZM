from utils.model import users
from utils.controller import get_user_info


def main():
    print('=============MENU=============')
    print('0 - zamknij aplikację')
    print('1 - wyświetl co u znajomych')
    print('==============================')
    while True:
        choice: str = input('Wybierz opcję menu: ')
        if choice == '0': break
        if choice == '1': get_user_info(users)

if __name__ == '__main__':
    main()




