import numpy as np

sample = np.random.randint(0, 10, 10)


# print(sample)


def insert_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        x = arr[i]
        while j >= 0 and x < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = x
    return arr


def select_sort(arr):
    for i in range(0, len(arr) - 1):
        minimum = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j
        temp = arr[i]
        arr[i] = arr[minimum]
        arr[minimum] = temp
    return arr


if __name__ == '__main__':
    arr = [5, 2, 9, 1, 5, 6]
    # sort = insert_sort(arr)
    sort = select_sort(arr)
    print(sort, end='  ')
