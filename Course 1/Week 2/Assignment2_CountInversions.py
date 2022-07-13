import numpy as np


def sort_and_count(a):
    n = len(a)
    if n == 1:
        return a, 0
    b, x = sort_and_count(a[:n//2])
    c, y = sort_and_count(a[n//2:])
    count = x + y
    d = []
    i, j = 0, 0
    while i < len(b) and j < len(c):
        if b[i] <= c[j]:
            d.append(b[i])
            i += 1
        else:
            d.append(c[j])
            j += 1
            count += len(b) - i
    if i == len(b):
        d.extend(c[j:])
    if j == len(c):
        d.extend(b[i:])
    return d, count


a = np.loadtxt("IntegerArray.txt")
a = list(map(int, a))
print(sort_and_count(a))