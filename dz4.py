# Реализуйте алгоритм перемешивания списка.

from random import random


def list_shuffle(list_to_shuffle, shuffle_times):
    for i in range(0, shuffle_times):
        index1 = 0
        index2 = 0
        while index1 == index2:
            index1 = int(random()*len(list_to_shuffle))
            index2 = int(random()*len(list_to_shuffle))
        temp = list_to_shuffle[index1]
        list_to_shuffle[index1] = list_to_shuffle[index2]
        list_to_shuffle[index2] = temp
    return list_to_shuffle


list_len = int(input('Введите длину массива: '))
my_list = []
for i in range(0, list_len):
    my_list.append(int(random()*list_len*2-list_len))
print(my_list)

shuffle_times = int(input('Сколько раз мешать список: '))
print(list_shuffle(my_list, shuffle_times))
