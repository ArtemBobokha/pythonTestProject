#_____________________________________________1___________________________________________________-
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


#_____________________________________________2___________________________________________________-

def count_result(arr, sum_elements):
    result = sum_elements * arr[-2]
    return result


def sum_1(args):
    total = 0
    for i in range(len(args)):
        if args[i] == '1':
            total += 1
    return total


a = [1, 7, 12]
sum_elem = 0
for i in range(len(a)):
    if sum_1(tuple(bin(a[i]))) % 2 == 0:
        sum_elem += a[i]

print(count_result(a, sum_elem))





