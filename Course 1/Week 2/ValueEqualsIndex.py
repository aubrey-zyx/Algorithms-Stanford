"""
You are given a sorted (from smallest to largest) array A of n distinct integers which can be positive, negative, or zero.
You want to decide whether or not there is an index i such that A[i] = i.
Design the fastest algorithm that you can for solving this problem.
"""

import numpy as np

def find_equal(a):
    n = len(a)
    left, right = 0, n - 1
    while left <= right:
        mid = (right - left) // 2 + left
        if a[mid] == mid:
            return True
        elif a[mid] < mid:
            left = mid + 1
        else:
            right = mid - 1
    return False

def brute_force(a):
    n = len(a)
    for i in range(n):
        if a[i] == i:
            return True
    return False

n = 1000
a = np.random.randint(-n, n, n)
a.sort()
print(find_equal(a))
assert find_equal(a) == brute_force(a)