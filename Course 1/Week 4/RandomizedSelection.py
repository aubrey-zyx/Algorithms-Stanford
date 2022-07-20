import random

def r_select(a, i):
    n = len(a)
    if n < 2:
        return a[0]
    pivot = random.randint(0, n-1)
    p = partition(a, 0, n-1, pivot)
    if p+1 == i:
        return a[p]
    elif p+1 > i:
        return r_select(a[:p], i)
    else:
        return r_select(a[p+1:], i-p-1)

def partition(a, left, right, pivot):
    a[left], a[pivot] = a[pivot], a[left]
    i = left + 1
    for j in range(left + 1, right + 1):
        if a[j] < a[left]:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i-1], a[left] = a[left], a[i-1]
    return i-1

a = [i for i in range(1, 101)]
random.shuffle(a)
print(r_select(a, 50))