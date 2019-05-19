#___________________________________1____________________________________________
from collections import Counter

a = 'spam and eggs or eggs with spam'

count = Counter(a)
print(count)

#___________________________________2____________________________________________
def binarySearch(mylist, x, start, stop):
    if start > stop:
        return False
    else:
        middle = (start + stop) // 2
        if x == mylist[middle]:
            return middle
        elif x < mylist[middle]:
            return binarySearch(mylist, x, start, middle - 1)
        else:
            return binarySearch(mylist, x, middle + 1, stop)


mylist = [1, 2, 5, 7, 12, 46, 58, 98, 103, 157]
start = 0
stop = len(mylist)
x = 103  # число, которое ищем

y = binarySearch(mylist, x, start, stop)

if y == False:
    print('число не найдено в массиве')
else:
    print('Даное число надохится в массиве под индексом: ' + str(y))

#___________________________________3____________________________________________

x = 'abba'
len(x)
y = list(x)
y1 = y[::-1]

if y == y1:
    print('Строка является палиндромом')
else:
    print('Строка НЕ является палиндромом')

#___________________________________4____________________________________________

def reverse(text):
    answer = ''
    temp = ''
    for char in text:
        if char != ' ':
            temp += char
            continue
        rev = ''
        for i in range(len(temp)):
            rev += temp[len(temp)-i-1]
        answer += rev + ' '
        temp = ''
    return answer + temp

#___________________________________5____________________________________________



#___________________________________6____________________________________________

def f(text):
    total, temp = 0, ''
    for ch in text:
        if ch.isdigit():
            temp += ch
        elif temp != '':
            total += int(temp)
            temp = ''
    if temp != '':
        total += int(temp)
    return total


a = "English = 78 Science = 83 Math = 68 History = 65"
print(f(a))

