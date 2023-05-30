print('введите дату в виде 02.11.2022')
date = input().split('.')
if (int(date[0]) * int(date[1]) == int(date[2][2:4])):
    print('магическое число')
else:
    print('число не магическое')
