"""
You are a given a unimodal array of n distinct elements, meaning that its entries are
in increasing order up until its maximum element, after which its elements are in decreasing order.
Give an algorithm to compute the maximum element that runs in O(log n) time.
"""

def find_peak(a):
    n = len(a)
    mid = n // 2
    if a[mid-1] < a[mid] > a[mid+1]:
        return a[mid]
    elif a[mid-1] < a[mid] < a[mid+1]:
        return find_peak(a[mid:])
    else:
        return find_peak(a[:mid])

a = [1,4,7,9,13,15,16,3,2]
print(find_peak(a))