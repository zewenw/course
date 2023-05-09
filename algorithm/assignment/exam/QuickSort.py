def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print(f'q is {i + 1}')
    return i + 1


def quicksort(arr, low, high):
    print(f'arr is {arr}')
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


# Example usage:
arr = [6, 5, 2, 4, 3, 1]
quicksort(arr, 0, len(arr) - 1)
print(arr)
