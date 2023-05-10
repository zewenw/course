import math


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print(f'q is {i + 1 + 1}')
    print(f'after partition, arr is {arr}')
    j = i
    while j >= low and arr[j] == arr[i + 1]:
        j = j - 1
    return math.ceil((i + j +1)/2)


def quicksort(arr, low, high):
    # print(f'arr is {arr}')
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        # print(f'after partition, arr is {arr[low: pi - 1]}')
        quicksort(arr, pi + 1, high)
        # print(f'after partition, arr is {arr[pi + 1: high]}')


# Example usage:
arr = [10,4,7,1,2,8,3]
quicksort(arr, 0, len(arr) - 1)
print(arr)
