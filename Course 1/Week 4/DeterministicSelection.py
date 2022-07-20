import random

def d_select(a, i):
    n = len(a)
    if n < 2:
        return a[0]
    groups = []
    for j in range(n//5):
        groups.append(list(a[5*j:5*j+5]))
    if n % 5:
        groups.append(list(a[5*(n//5):]))
    medians = []
    for group in groups:
        group.sort()
        medians.append(group[len(group)//2])
    median = d_select(medians, (len(medians)+1)//2)     # Median of medians
    for j in range(n):
        if a[j] == median:
            pivot = j
            break
    p = partition(a, 0, n-1, pivot)
    if p+1 == i:
        return a[p]
    elif p+1 > i:
        return d_select(a[:p], i)
    else:
        return d_select(a[p+1:], i-p-1)

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
print(d_select(a, 30))