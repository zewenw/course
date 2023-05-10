import math


def partition(A, p, r):
    x = A[r]  # pivot
    i = p - 1

    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    j = i

    while j >= p and A[j] == A[i + 1]:
        j -= 1
    print(f'arr is {arr}')
    return math.ceil((i + j + 1)/2)


arr = [ 0, 0, 0, 0, 0,0,0,0]
res = partition(arr, 0, len(arr) - 1)
print(f'res is {res}')