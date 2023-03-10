# 1. Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#   Пример:
#       - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# способ через генераторы и циклы
# import random

# def sum_odd_elem_inlist(def_list):
#     sum = 0
#     for i in range(len(def_list)):
#         if i % 2 !=0:
#             sum += def_list[i]
#     return sum

# lenght_list = 10
# my_list = [random.randint(0,10) for i in range(lenght_list)]
# my_odd_list = [my_list[i] for i in range(lenght_list) if i % 2 !=0]
# print(f'{my_list} -> на нечётных позициях элементы {my_odd_list}ответ: {sum_odd_elem_inlist(my_list)}')


# 2 Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#   *Пример:*
#       - [2, 3, 4, 5, 6] => [12, 15, 16];
#       - [2, 3, 5, 6] => [12, 15]

# from math import ceil

# def sum_of_pare(array):

# # get list of integer digits and return new list with
# # multiplication of elements with elements that has negative some indexes
# # :param array: list
# # :return: new list

# accumulator = []
# for i in range(ceil(len(array) / 2)):
#     accumulator.append(array[i] * array[-(i + 1)])
# return accumulator


# print(sum_of_pare([2, 3, 4, 5, 6]))
# print(sum_of_pare([2, 3, 5, 6]))


# 3 Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#   *Пример:*
#       - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# lenght_list = 5
# my_list = [1.1, 1.2, 3.1, 5, 10.01]
# my_tail_list = [round(my_list[i])-int(my_list[i], 2) for i in range(lenght_list) if my_list[i] % 1 !=0]
# print(f'{my_tail_list} -> {max(my_tail_list - min (my_tail_list))}')

lenght_list = 5

my_list = [1.1, 1.2, 3.1, 5, 10.01]
my_tail_list = [round(my_list[i]-int(my_list[i]),2) for i in range(lenght_list) if i % 1 != 0] 
print(f'{my_list} -> {max(my_tail_list) - min(my_tail_list)}')

# 4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
# 5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи](https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8#:~:text=%D0%92%20%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B5%2C%20%D1%87%D0%B8%D1%81%D0%BB%D0%B0%20%D0%BD%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8%20%E2%80%94%20%D0%BE%D1%82%D1%80%D0%B8%D1%86%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%20%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D1%87%D0%B8%D1%81%D0%B5%D0%BB%20%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8.)