class Client:
    def __init__(self, name, second_name, city, balance):
        self.name = name
        self.second_name = second_name
        self.city = city
        self.balance = balance
    def __int__(self):
        return f"{self.name} {self.second_name}.{self.city}.Баланс:{self.balance}руб"
client_1 = Client('Иван', 'Иванов', 'Москва', 50)
print(client_1.__int__())