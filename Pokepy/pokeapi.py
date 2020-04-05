import requests
import json
from random import randrange

class PokeAPI(object):
    def __init__(self):
        #self.ENDPOINT = 'https://pokeapi.co/api/v2/pokemon-form'
        self.ENDPOINT='https://pokeapi.co/api/v2/pokemon'

    def getPokemon(self, x):
        uri = f'{self.ENDPOINT}/{x}'
        r = requests.get(uri)
        data = r.json()

        return {
            'name': data.get('name'),
            'id' : data.get('id'),
            'base_experience' : data.get('base_experience'),
            'weight': data.get('weight'),
            'type': data.get('species', {}).get('url'),
            'image': data.get('sprites', {}).get('front_default')
        }

api = PokeAPI()
print(json.dumps(api.getPokemon((25)), indent=2))