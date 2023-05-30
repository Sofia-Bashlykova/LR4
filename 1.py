print('введите число')
try:
    x = int(input())
except ValueError:
    print("введено не число")
if  (x % 3 == 0) and x != 0:
    print("число делится на 3")
elif x == 0:
    print("введен 0")
else:
    print("число не делится на 3")