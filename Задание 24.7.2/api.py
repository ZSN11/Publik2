import requests
from settinds import valid_email, valid_password, base_url,animal_type,age,name,photo_k
import json


class Req_My_Pets:
    def get_key(self,email,password):
        self.email=valid_email
        self.password=valid_password
        headers = {
            'email': valid_email,
            'password': valid_password
        }
        res = requests.get(base_url + "api/key", headers=headers)
        global auth_key
        auth_key = res.json()
        print(res.status_code)
        print('key =',auth_key['key'])
        return res.status_code,auth_key

    def post_my_pets(auth_key):
 #       self.auth_key=auth_key
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }
        headers = {'auth_key': auth_key['key']}
        res = requests.post(base_url + "api/create_pet_simple", headers=headers, data=data)
        status=res.status_code
        print(status,'Добавлен новый питомец кот без фото')
        my_pets = res.json()
        global _pet_id
        global _user_id
        global _created_at
        _created_at=my_pets.get('created_at')
        _user_id=my_pets.get('user_id')
        _pet_id = my_pets.get('id')
        new_pet_name = my_pets.get("name")
        print(my_pets)
        print("имя нового питомца =",new_pet_name)
        return status,my_pets

    def post_my_pets_photo(self,auth_key):
        self.auth_key=auth_key
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age,
            'id ': _pet_id,
            'user_id' : _user_id,
            "created_at" :_created_at
        }
        files = {'pet_photo': open(photo_k, 'rb')}
        headers = {'auth_key': auth_key['key']}
        res = requests.post(base_url + "api/pets/set_photo/"+_pet_id, headers=headers, data=data,files=files)
        print(res.status_code,'Добавлено фото кота Василия')
        my_pets = res.json()
        print(my_pets)
#        print(my_pets.get('pet_photo'))




Req_My_Pets.get_key(self=Req_My_Pets, email=valid_email,password=valid_password)
Req_My_Pets.post_my_pets(auth_key=auth_key)
Req_My_Pets.post_my_pets_photo(self=Req_My_Pets,auth_key=auth_key)
