import dataclasses
from dataclasses import dataclass

import requests

SCRYFALL_API = 'https://api.scryfall.com'
PLANAR_QUERY = 'q=t:plane%20or%20t:phenomenon'


@dataclass
class ScryfallApiPlanarCard:
    id: str
    name: str
    image_uris: dict
    type_line: str
    oracle_text: str

    def __init__(self, **kwargs):
        names = set([f.name for f in dataclasses.fields(self)])
        for k, v in kwargs.items():
            if k in names:
                setattr(self, k, v)


def get_all_planar_cards():
    url = f'{SCRYFALL_API}/cards/search?{PLANAR_QUERY}'
    response = requests.get(url)
    if response.status_code != 200:
        return None
    json = response.json()
    data = json['data']
    cards = [ScryfallApiPlanarCard(**item) for item in data]
    return cards
