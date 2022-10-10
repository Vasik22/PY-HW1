# day = int(input('Введите день: '))
# if day == 1:
#     print('Понедельник')
# elif day == 2:
#     print('Вторник')
# elif day == 3:
#     print('Среда')
# elif day == 4:
#     print('Четверг')
# elif day == 5:
#     print('Пятница')
# elif day == 6:
#     print('Суббота')
# elif day == 7:
#     print('Воскресенье')    
# else:
#     print('Некорректный ввод')







# import math

# x = float(input('Введите координату точки А по оси Х: '))
# y = float(input('Введите координату точки А по оси Y: '))
# x1 = float(input('Введите координату точки B по оси Х: '))
# y1 = float(input('Введите координату точки B по оси Y: '))

# distance = round(math.sqrt((x1 - x)**2 + (y1 - y)**2), 2)
# print(distance)




# quarter = int(input('Введите номер четверти: '))

# if quarter == 1:
#     print('x > 0, y > 0')
# elif quarter == 2:
#     print('x < 0, y > 0')
# elif quarter == 3:
#     print('x < 0, y < 0')
# elif quarter == 4:
#     print('x > 0, y < 0')
# else:
#     print('Некорректный ввод')


n = int(input('Введите число: '))
for i in range (2, n, 2):
        print(i, end=' ')
        