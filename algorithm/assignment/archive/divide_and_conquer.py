a = [3, 16, 2, 7, 15, 20, 6, 89, 74, 2, 14]
r = len(a) - 1
p = 0
x = a[r]

pivot = a[r]
i = p - 1
for j in range(p, r):
    if a[j] <= pivot:
        i = i + 1
        a[i], a[j] = a[j], a[i]
a[i + 1], a[r] = a[r], a[i + 1]
print(a)
