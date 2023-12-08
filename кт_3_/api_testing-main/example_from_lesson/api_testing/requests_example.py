import requests
import pprint
import json

BASE_URL_PETSTORE = 'https://petstore.swagger.io/v2'

# GET
response = requests.get(f'{BASE_URL_PETSTORE}/pet/1')
pprint.pprint('GET example_from_lesson')

pprint.pprint(response.url)
pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint(response.text)
pprint.pprint(response.json())
pprint.pprint('**********')
# comment
# Get with filters
# get https://petstore.swagger.io/v2/pet?bod=20220506&breed=corgi
pass

# POST
data = {'name': 'Barsic'}
response = requests.post(f'{BASE_URL_PETSTORE}/pet/1', data=data)

pprint.pprint('POST example_from_lesson')
pprint.pprint(response.status_code)
pprint.pprint(response.reason)

dict_text = json.loads(response.text)
pet_id = dict_text['message']
# verify post
response = requests.get(f'{BASE_URL_PETSTORE}/pet/{pet_id}')

pprint.pprint(f'GET {pet_id}')
pprint.pprint(response.status_code)
pprint.pprint(response.text)

pet_info = json.loads(response.text)
assert data['name'] == pet_info['name']
assert data['name'] == response.json()['name']
pprint.pprint('**********')
# comment
# POST, PATCH, PUT
pass

# DELETE
response = requests.delete(f'{BASE_URL_PETSTORE}/pet/1')

pprint.pprint('DELETE example_from_lesson')
pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint(response.text)

response = requests.get(f'{BASE_URL_PETSTORE}/pet/1')
pprint.pprint(f'GET 1')

pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint(response.text)
pprint.pprint('**********')
pass



