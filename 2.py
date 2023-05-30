try:
    print('введите число')
    x = int(input())
    y = 100 / x
except ValueError:
    print('введено не число')
except ZeroDivisionError:
    print('введён 0')
else:
    print(x, ' : 100 = ', y)