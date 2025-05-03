
users:list=[
    {'name':'Beata','location':'Lublin','posts':555},
    {'name':'Mikołaj','location':'Przasnysz','posts':200},
    {'name':'Krzysztof','location':'Poznań','posts':100},
    {'name':'Bartosz','location':'Ostrołęka','posts':300},
]


def get_user_info(users_data:list)->None:
    for user in users_data:
        print(f'Twój znajomy {user["name"]} z miejscowości {user["location"]} opublikował {user["posts"]} postów.')

get_user_info(users)