# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

print('Введите номер четверти:')
a = int(input())
if a==1: print('X>0 and Y>0')
elif a==2: print('X<0 and Y>0')
elif a==3: print('X<0 and Y<0')
elif a==4: print('X>0 and Y<0')
else: print('Четвертей всего 4')