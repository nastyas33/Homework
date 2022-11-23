from math import pi
''' круг '''

radius = int(input('Введите радиус: '))
A = pi * radius ** 2
L = radius * pi * 2
print('Площадь круга -', round(A))
print('Периметр круга -', round(L))

''' квадрат '''
b = int(input('Введите длину стороны квадрата: '))
P = 4 * b
Square = b ** 2
print('Площадь квадрата -', Square)
print('Периметр квадрата -', P)