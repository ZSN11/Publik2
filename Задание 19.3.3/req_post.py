import requests

data = {

        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
}

res = requests.post(f'http://petstore.swagger.io/v2/pet/5',headers={'accept': 'application/json','Content-Type': 'application/json'},data=data)

print(res.status_code)
print(res.json())