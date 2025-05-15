class User:
    def __init__(self, name: str, surname: str, location: str, posts: str, ):
        self.name = name
        self.surname = surname
        self.location = location
        self.posts = posts
        self.coordinates = self.get_coordinates()
        self.marker=map_widget.set_marker(self.coordinates[0], self.coordinates[1])


    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup

        url = f'https://pl.wikipedia.org/wiki/{self.location}'
        response = requests.get(url).text
        response_html = BeautifulSoup(response, 'html.parser')
        longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
        latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
        return [latitude, longitude]