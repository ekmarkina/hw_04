"""
Реализовать сортировку списка методом пузырька.
"""

def bubble(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            array[j], array[j + 1] = (array[j + 1], array[j]) if array[j] > array[j + 1] else (array[j], array[j + 1])


arr = [5, 8, 2, 3, 4, 9, 7, 6, 1, 0]
print(f"Исходный массив: {arr}")
bubble(arr)
print(f"Отсортированный массив: {arr}")
