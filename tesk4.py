# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

a1 = float(input('A1:'))
a2 = float(input('A2:'))
b1 = float(input('B1:'))
b2 = float(input('B2:'))

d = round(math.sqrt(math.pow((b1-a1),2)+math.pow((b2-a2),2)),2)

print(f'A({round(a1)}, {round(a2)}); B({round(b1)}, {round(b2)}) -> {d}')
