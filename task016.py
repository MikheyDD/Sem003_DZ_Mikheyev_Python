"""Задача 16
Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
Пример:
5
1 2 3 4 5
3
-> 1"""

from random import randint
N = int(input('Введите натуральное число: '))
numbers = []
for _ in range(N):
    numbers.append(randint(1, N))
# numbers = [randint(1, N) for i in range(N)]
print(numbers)
x = int(input('Введите число x: '))
c = numbers.count(x)
print(c)

