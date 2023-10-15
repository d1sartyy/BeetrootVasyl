#Task-1

import random

def dir_bubble_sort(l):
    n = len(l)
    swapped = True

    while swapped:
        swapped = False

        for i in range(0, n - 1):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                swapped = True

        for i in range(n - 2, -1, -1):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                swapped = True

    return l

random_list = [random.randint(-10000, +10000) for _ in range(2000)]
sorted_list = dir_bubble_sort(random_list)
print(sorted_list)


#Task-2

def merge_sort(l):
    if len(l) > 1:
        mid = len(l) // 2
        left_half = l[:mid]
        right_half = l[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        k, i, j = 0, 0, 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                l[k] = left_half[i]
                i += 1
            else:
                l[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            l[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            l[k] = right_half[j]
            j += 1
            k += 1

random_list = [random.randint(-10000, +10000) for _ in range(2000)]

merge_sort(random_list)

print(random_list)

#Task - 3

import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def quicksort(l, partition_limit=10):
    if len(l) <= partition_limit:
        insertion_sort(l)
        return l
    elif len(l) > 1:
        pivot = l[len(l) // 2]
        left, right = [], []

        for element in l:
            if element < pivot:
                left.append(element)
            elif element > pivot:
                right.append(element)

        equal_elements = [element for element in l if element == pivot]

        return quicksort(left, partition_limit) + equal_elements + quicksort(right, partition_limit)

random_list = [random.randint(-10000, +10000) for _ in range(2000)]

sorted_list = quicksort(random_list)

print(sorted_list)



