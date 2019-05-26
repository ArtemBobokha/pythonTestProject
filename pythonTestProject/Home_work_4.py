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

def count_result(arr, sum_elements):
    result = sum_elements * arr[-2]
    return result


def sum_1(args):
    total = 0
    for i in range(len(args)):
        if args[i] == '1':
            total += 1
    return total


a = [1, 7, 15]
sum_elem = 0
for i in range(len(a)):
    if sum_1(bin(a[i])) % 2 == 0:
        sum_elem += a[i]

print(count_result(a, sum_elem))


# ________________________________________________3(a,b,c)__________________________________________________

a = 'dkjfh12'
character_array = 'qwertyuipasdfghjklzxcvbnm0123456789'
litters = 'qwertyuipasdfghjklzxcvbnm'
numbers = '0123456789'


# Функция проверки длины пароля
def len_password(arr):
    if len(a) > 4:
        return True


# Функция проверни наличие маленьких латинских букв и цифр
def check_latin_litters_and_numbers(arr):
    if a.isalnum() == True and a.islower() == True:
        return True
    else:
        return False


# Функция подсчёта букв в пароле
def sum_lit(arr, litters_arr):
    total = 0
    for i in range(len(a)):
        if a[i] in litters:
            total += 1
    return total


# Функция проверки на нечётное кол-во букв пароле
def nechet_litters(fun_5):
    if fun_5 % 2 == 1:
        return True
    else:
        return False


# Функция подсчёта цифр в пароле
def sum_num(arr, numbers_arr):
    total = 0
    for i in range(len(a)):
        if a[i] in numbers:
            total += 1
    return total


# Функция проверки на нечётное кол-во цифр пароле
def chet_numbers(fun_6):
    if fun_6 % 2 == 0:
        return True
    else:
        return False


def password_validator(fun_1, fun_2, fun_3, fun_4 ):

    if len_password(a) == True and check_latin_litters_and_numbers(a) == True and nechet_litters(sum_lit(a, litters)) and chet_numbers(sum_num(a, numbers)):
        # как написать данное выжажение более компактно или правильно ?
        print('Пароль валидный')
    else:
        print('Пароль не валидный')


password_validator(len_password(a), check_latin_litters_and_numbers(a), sum_num(a, numbers),sum_lit(a, litters))

# _____________________________________________________4_________________________________________________________
