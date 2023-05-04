import requests
from settings import valid_email, valid_password, base_url,name,name1,animal_type,age,pet_photo
global _auth_key
global status_code


class Req_My_Pets:
    def get_key(self,email,password):
        self.email=email
        self.password=password
        headers = {
            'email': valid_email,
            'password': valid_password
        }
        res = requests.get(base_url + "api/key", headers=headers)
        auth_key = res.json()
        global _auth_key
        _auth_key=auth_key
        print(res.status_code)
        print('key =',_auth_key['key'])

    def get_my_pets(self,auth_key):
        self.auth_key=_auth_key
        headers = {
            "accept": 'application/json',
            'auth_key': _auth_key['key']
        }
        res = requests.get(base_url + 'api/pets?filter=my_pets', headers=headers)
        status_code=res.status_code
        print(status_code)
        print('Список моих питомцев:',res.json())


    def post_my_pets(self,auth_key):
        global _pet_id
        self.auth_key=_auth_key
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }
        headers = {'auth_key': _auth_key['key']}
        files = {'pet_photo': open(pet_photo, 'rb')}
        res = requests.post(base_url + "api/pets", headers=headers, data=data, files=files)
        print(res.status_code,'Добавлен новый питомец собака Сигма')
        my_pets = res.json()
        _pet_id = my_pets.get("id")
        print(my_pets)
        print("id нового питомца =",_pet_id)


    def put_my_pets(self,pet_id,auth_key):
        self.auth_key=_auth_key
        self.pet_id=_pet_id
        data = {

            'animal_type': animal_type,
            'age': age,
            'name': name1,
        }
        headers = {'auth_key':_auth_key['key']}
        files = {'pet_photo': open(pet_photo, 'rb')}
        res = requests.put(base_url+"api/pets/"+_pet_id,headers=headers, data=data, files=files)
        print(res.status_code,'Изменяем имя питомца на Шарик')
        print(res.json())

    def del_my_pets(self,pet_id,auth_key):
        self.pet_id=_pet_id
        self.auth_key=_auth_key
        headers={'auth_key':_auth_key['key']}
        res=requests.delete(base_url+"api/pets/"+_pet_id,headers=headers)
        print(res.status_code,'Удаляем питомца Шарик')




Req_My_Pets.get_key(self=Req_My_Pets,email='email',password='password') #Получаем ключ
Req_My_Pets.get_my_pets(self=Req_My_Pets,auth_key=_auth_key['key'])     #Получаем список питомцев
Req_My_Pets.post_my_pets(self=Req_My_Pets,auth_key=_auth_key['key'])    #Добавляем питомца
Req_My_Pets.put_my_pets(self=Req_My_Pets,auth_key=_auth_key['key'],pet_id=_pet_id)     #Изменяем имя питомца на Шарик
Req_My_Pets.del_my_pets(self=Req_My_Pets,auth_key=_auth_key['key'],pet_id=_pet_id)      #Удаляем питомца Шарик
