# Задача 16: 
# Требуется вычислить, сколько раз встречается некоторое число X в списке A. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

# *Пример:*
# 5

# 1 2 3 4 5
# 3
#-> 1

# N = (int(input('Введите количество элементов в списке А: ')))
# list = [] 
# for i in range(N):
#     list.append(int(input('Введите целое число из списка А: ')))
#     i += i
# X = (int(input('Введите число, которое необходимо найти в списке А: ')))
# count = 0
# for i in range(N):
#     if list[i] == X:
#         count += 1
# print(f'Число {X} встречается в списке А {count} раз')


# Задача 18: Требуется найти в списке A самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
# *Пример:*
# 5
# 1 2 3 4 5
# 6
# -> 5


N = int(input('Введите количество элементов списка А: '))
A_entered = []
for _ in range (N):
 A_entered.append(int(input()))
print( A_entered)
X = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))
min = X - A_entered[0]
index = 0
for i in range(1, N):
    count = X - A_entered[i]
if count < min:
            min = count
            index = i
print(f'Число {A_entered[index]} в списке A наиболее близко по величине к числу {X}, их разница составляет {X - A_entered[index]}')