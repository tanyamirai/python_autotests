import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'a2a707769705ec85f496bec19d57a4e4'
HEADER = {'Content-Type' : 'application/json' , 'trainer_token':TOKEN}
create_pokemon = {
    "name": "generate",
    "photo_id": -1
}
rename_pokemon = {
    "pokemon_id": "72728",
    "name": "ImFromPython",
    "photo_id": 983
}
add_pokeball = {
    "pokemon_id": "72728"
}


'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = create_pokemon)
print(response.text)'''

'''response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = rename_pokemon)
print(response.text)'''

'''response_add = requests.post(url = f'{URL}/trainers/add_pokeball' , headers = HEADER, json = add_pokeball,)
print(response_add.text)'''