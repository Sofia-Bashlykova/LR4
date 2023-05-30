print('введите номер билета')
x = input()
x1 = len(x)
y = int(x1 / 2)
sum1 = 0
sum2 = 0
if x1 % 2 == 0:
    for i in range(y):
        sum1 += int(x[i])
    for j in range(y, x1):
        sum2 += int(x[j])
    if sum1 == sum2:
        print('билет счастливый')
    else:
        print('билет не является счастливым')
else:
    print('билет нечетный')
