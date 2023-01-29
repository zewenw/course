arr = [-1, 4, 3, -2]
two_arr = {}
for i in range(0, len(arr)):
    for j in range(i, len(arr)):
        two_arr[i, j] = 0
        for k in range(i, j):
            if k == 2:
                print(k)
            two_arr[i, j] = two_arr[i, j] + arr[k]
print(two_arr)
