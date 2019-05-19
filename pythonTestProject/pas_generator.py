import random
import sys

while True:
    print('Введите длину пароля:')
    len_pas = input()

    if len_pas.isdigit():
        if len_pas != 0:
            str_1 = 'qwertyuipasdfghjklzxcvbnm'
            srt_2 = str_1.upper()
            srt_3 = str(random.randrange(0, 9))
            all_srt = str_1 + srt_2 + srt_3

            a = list(all_srt)  # преобразование в список

            x = ''.join(random.choice(a) for i in range(int(len_pas)))

            print(x)
            sys.exit(0)
        else:
            sys.exit(0)
    else:
        print('Введите числовое значение длины пароля')


