import json

import requests


status = 'available'
data ={
  "id": 1,
  "username": "string",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "userStatus": 0
}


res = requests.put(f'https://petstore.swagger.io/v2/user/1',headers={'accept': 'application/json','Content-Type': 'application/json'}, data=json.dumps(data, ensure_ascii=False ))


print(res.status_code)
print(res.text)
