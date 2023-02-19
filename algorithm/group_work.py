import math


def new_sort(a, i, j):
    print(f"i = {i}  j = {j}")
    if i == j:
        return
    elif i + 1 == j:
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
            print(f"i = {i}  j = {j}")
            # print(a)

    elif i + 2 == j:
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
        if a[i + 1] > a[j]:
            a[i + 1], a[j] = a[j], a[i + 1]
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
        # print(a)
    else:
        k = math.floor((j - i + 1) / 4)
        new_sort(a, i, j - k)
        new_sort(a, i + k, j)
        new_sort(a, i, j - k)


a = [0, 8, 8, 7, 7]
new_sort(a, 0, len(a) - 1)
