class Client:
    def __init__(self, name, second_name, city, balance):
        self.name = name
        self.second_name = second_name
        self.city = city
        self.balance = balance
    def __int__(self):
        return f"{self.name} {self.second_name}.{self.city}.Баланс:{self.balance}руб"
    def guest(self):
        return f"{self.name} {self.second_name}.{self.city}."
guest_1 = Client('Иван', 'Иванов', 'Москва', 300)
guest_2 = Client('Сидор', 'Сидоров', 'Ленинград', 500)
guest_3 = Client('Матвей', 'Матвееев', 'дер. Гадюкино',1000)
guest_list = [guest_1, guest_2, guest_3]
for guest_ in guest_list:
    print(guest_.guest())