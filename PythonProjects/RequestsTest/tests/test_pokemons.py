import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN ='8232b83f90348cd7b450f868f4627c0b'
HEADER = {'Content-type':'application/json','trainer_token':TOKEN}
TRAINER_ID = '37454'

def test_ststus_code():
    response = requests.get(url=F'{URL}/pokemons', params={'trainer_id': TRAINER_ID})
    assert response.status_code==200

def test_part_of_respone():
    response_get = requests.get(url=F'{URL}/pokemons', params={'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'Бульбазавр'

@pytest.mark.parametrize('key,value',[('name','Бульбазавр'),('trainer_id', TRAINER_ID),('id', '306341')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url=F'{URL}/pokemons', params={'trainer_id': TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value

