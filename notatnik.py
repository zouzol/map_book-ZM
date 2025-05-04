users:list=[
    {'name':'Beata','location':'Lublin','posts':555},
    {'name':'Mikołaj','location':'Przasnysz','posts':200},
    {'name':'Krzysztof','location':'Poznań','posts':100},
    {'name':'Bartosz','location':'Ostrołęka','posts':300},
]

import folium

import requests
from bs4 import BeautifulSoup

# https://pl.wikipedia.org/wiki/Przybys%C5%82awice_(wojew%C3%B3dztwo_lubelskie)




get_map(users)