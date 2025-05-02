import requests
import json

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN ='8232b83f90348cd7b450f868f4627c0b'
HEADER = {'Content-type':'application/json','trainer_token':TOKEN}

body_registration ={
    "trainer_token": TOKEN,
    "email": "Golopopin0025@mail.ru",
    "password": "941177qQ"
}
body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_pokeball = {
    "pokemon_id": pokemon_id
}

body_rename = {
    "pokemon_id": pokemon_id,
    "name": "Бульбазавр2",
    "photo_id": "1"
}


response = requests.post(url=f'{URL}/trainers/reg',headers=HEADER,json=body_registration)
print(response.text)

response_confirmation = requests.post(url=f'{URL}/trainers/confirm_email',headers=HEADER,json=body_confirmation)
print(response_confirmation.text)

# 1. Создание покемона
response_create = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_create)
print("Создание покемона:", response_create.json())


# Получаем ID созданного покемона
pokemon_id = response_create.json().get('id')
print("ID покемона:", pokemon_id)

# 2. Добавление покемона в покебол
response_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_pokeball)
print("Добавление в покебол:", response_pokeball.json())


# 3. Изменение имени покемона
response_rename = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_rename)
print("Изменение имени:", response_rename.json())