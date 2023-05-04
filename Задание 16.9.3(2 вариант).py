
clients = []

while True:
    client = []
    name = input('Введите имя нового клиента''  ')
    client.append(name)
    second_name = input('Введите фамилию нового клиента''  ')
    client.append(second_name)
    citi = input('Введите город проживания нового клиента''  ')
    client.append(citi)
    balance = input('Введите баланс нового клиента''  ')
    client.append(balance)
    clients.extend([client])
    stop = input("Хотите ввести еще клиента, нажмите 'y"  ' ')

    if stop == 'y':
     continue
    else:
     break

for c in clients:
     print(*c, sep=",  ")
