import random


"""проходим циклом по всем элементам, пока не будет ни одного захода в обмен элементов"""
def bubble_sort(arr):
    flag = 1
    while flag == 1:
        flag = 0
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                (arr[i], arr[i+1]) = (arr[i+1], arr[i])
                flag = 1
    return arr


"""выбираем опорный элемент(любой), рекурсивно делим текущее состояние массива на 3 части и сортируем,
 пока не останется ни одного эл. в изначальном массиве"""
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    less = [el for el in arr if el < pivot]
    equal = [el for el in arr if el == pivot]
    bigger = [el for el in arr if el > pivot]
    return quick_sort(less) + equal + quick_sort(bigger)


""" Создаем вспомогательный массив длиной в максимальный элемент + 1. Изначально заполняем нулями,
 проходим циклом несортированный массив и итерируем значения элементов под индексами-элементами в массиве-счетчике"""
def counting_sort(arr):
    if len(arr) <= 1:
        return arr
    count_arr = [0 for i in range(max(arr) + 1)]  # массив-счетчик
    for el in arr:  # итерируем вхождения элементов в изначальный массив
        count_arr[el] += 1

    sorted_arr = []
    for i in range(len(count_arr)):  # заполняем новый массив элементами - индексами столько раз, сколько под
        # индексом вхождений
        for j in range(count_arr[i]):
            sorted_arr.append(i)
    return sorted_arr


array = [1, 4, 8, 9, 3]
print(array)

print(bubble_sort(array.copy()))
print(quick_sort(array.copy()))
print(counting_sort(array.copy()))
