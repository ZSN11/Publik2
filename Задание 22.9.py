numbers = '27 12 -10 5 1 0 -6 9 -1 '
number =",".join(map(str, numbers.split())) # Пробелы меняем на запятые
Lis = number.split(',')   # Преобразуем в список
List = [int(x)for x in Lis]  #приводим к целочисленному виду
List_sort = sorted(List)

for i in range(1, len(List)):   # Сортируем
    x = List[i]
    idx = i
    while idx > 0 and List[idx - 1] > x:
        List[idx] = List[idx - 1]
        idx -= 1
    List[idx] = x

#Ищим позициюб который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу.

def search(List_sort, user):
    low = 0
    hight = len(List_sort) - 1
    ind = -1
    while (low <= hight) and (ind == -1):
        mid = (low + hight)//2
        if List_sort[mid] == user:
            ind = mid - 1
        elif List_sort[mid] < user < List_sort[mid +1]:
            ind = mid
        else:
            if user < List_sort[mid]:
                hight = mid - 1
            else:
                low = mid + 1
    return ind

 # Ошибки при вводе данных

while True:
    try:
        user = int(input('Введите любое число '))
        if min(List) > user or max(List) < user:
            print(print('Введённое число не входит в заданную последовательность'))
            continue
    except ValueError:
        print("Будте внимательны - Вы ввели не число")
        continue
    if ValueError == True:
        continue
    else:
        print('Последовательность', numbers, '\n','Списсок', List_sort, '\n','Номер позиции', search(List_sort, user))
        break