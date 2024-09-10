#Пункты задачи:
#Если все числа равны между собой, то вывести 3
#Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
#Если равных чисел среди 3-х вообще нет, то вывести 0

first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

if first != second and first != third and second != third:
    print(0)
elif first == second and first == third and second == third:
    print(3)
else:
    print(2)
