
def get_user_info(users_data:list)->None:
    for user in users_data:
        print(f'Twój znajomy {user["name"]} z miejscowości {user["location"]} opublikował {user["posts"]} postów.')


def add_user(users_data: list) -> None:
    new_name = input('Podaj imie nowego uzytkownika: ')
    new_location
    input('Podaj lokalizacje nowego uzytkownika:')
    new_posts = int(input('Podaj liczbe postow nowego uzytkownika: '))
    users_data.append({'name': new_name, 'location': new_posts, 'posts': new_posts})
