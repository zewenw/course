import math


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    # print(f'q is {i + 1 + 1}')
    # print(f'after partition, arr is {arr}')
    j = i
    while j >= low and arr[j] == arr[i + 1]:
        j = j - 1

    print(f'arr is {arr}')
    return math.ceil((i + j + 1) / 2)


arr = [8, 8, 7, 7, 0, 0, 0, 0, 0]
res = partition(arr, 0, len(arr) - 1)
print(f'res is {res}')
