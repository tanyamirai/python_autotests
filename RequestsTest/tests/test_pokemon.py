import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'a2a707769705ec85f496bec19d57a4e4'
HEADER = {'Content-Type' : 'application/json' , 'trainer_token':TOKEN}
TRAINER_ID = '5725'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_trainer_name():
   response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
   assert response_get.json()["data"][0]["trainer_name"] == 'Bulochka'


@pytest.mark.parametrize('key, value', [('trainer_name', 'Bulochka'), ('id', TRAINER_ID)])
def test_parametrize(key, value):
  response_parametrize = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
  assert  response_parametrize.json()["data"][0][key] == value