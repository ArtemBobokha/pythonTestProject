# _____________________________________________1___________________________________________________-
target_list = [12, 24, 37, 'sggg']


def swap(target_list, item_index1, item_index2):
    target_list[item_index1], target_list[item_index2] = target_list[item_index2], target_list[item_index1]
    return target_list


while True:
    print('Выберите индексы элементов массива, которые необходимо поменять местами:')

    print('Ведите первый индкес:')
    item_index1 = int(input())
    if item_index1 >= len(target_list) or item_index1 < 0 or item_index1 == '':
        print('Данного элемента нет в массиве')
        continue

    print('Ведите второй индкес:')
    item_index2 = int(input())
    if item_index2 >= len(target_list) or item_index2 < 0 or item_index2 == '':
        print('Данного элемента нет в массиве')
        continue

    item_value1 = target_list[item_index1]
    item_value2 = target_list[item_index2]
    print(swap(target_list, item_index1, item_index2))
    break


swap(target_list, item_index1, item_index2)


# _____________________________________________2___________________________________________________-

a = [1, 2, 3, 4]  # результат 15
total = 0


def sum_1(args):
    total1 = 0
    for i in range(len(args)):
        if args[i] == '1':
            total1 += 1
    return total1


for j in range(len(a)):
    print(j)
    if sum_1(bin(j)) % 2 == 0:
        total += a[j]

print(total * a[-2])

# _______________________________________________3(a,b,c)__________________________________________________
import string
a = 'dkjfh12'
litters = 'qwertyuipasdfghjklzxcvbnm'


def password_validator(x):
    total_litters = 0
    total_numbers = 0
    for i in range(len(x)):
        if x[i] in litters:
            total_litters += 1

    for i in range(len(x)):
        if x[i] in string.digits:
            total_numbers += 1

    if len(x) > 4 and x.isalnum() == True and total_litters % 2 != 0 and total_numbers % 2 == 0:
        print('Пароль валиный')
    else:
        print('Пароль не валидный')


password_validator(a)


# _____________________________________________________4_________________________________________________________
