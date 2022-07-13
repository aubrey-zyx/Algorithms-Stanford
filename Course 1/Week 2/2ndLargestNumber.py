import numpy as np
from collections import defaultdict

def find_2nd_largest(a):
    ht = defaultdict(list)

    def find_max(a):
        n = len(a)
        if n == 0:
            return -1, 0
        if n == 1:
            return a[0], 0
        if n == 2:
            if a[0] > a[1]:
                ht[a[0]].append(a[1])
                return a[0], 1
            else:
                ht[a[1]].append(a[0])
                return a[1], 1
        a1, x = find_max(a[:n//2])
        a2, y = find_max(a[n//2:])
        if a1 > a2:
            ht[a1].append(a2)
            return a1, x + y + 1
        else:
            ht[a2].append(a1)
            return a2, x + y + 1

    max, count1 = find_max(a)
    second_largest, count2 = find_max(ht[max])
    return second_largest, count1 + count2

power = 10
n = 2 ** power
a = [i for i in range(1, n + 1)]
np.random.shuffle(a)
sortedlist = a.copy()
sortedlist.sort()
result = find_2nd_largest(a)
print("second-largest number: " + str(result[0]))
assert result[0] == sortedlist[-2]
print("using %d comparisons" % result[1])
assert result[1] <= n + np.log2(n) - 2