def quick_sort(a, left, right, mode):
    n = right - left + 1
    if n < 2:
        return
    pivot = partition(a, left, right, mode)
    quick_sort(a, left, pivot-1, mode)
    quick_sort(a, pivot+1, right, mode)
    return

def partition(a, left, right, mode):
    global count
    if mode == "first":
        pivot = left
    elif mode == "last":
        pivot = right
    elif mode == "median":
        pivot = find_median(a, left, right)
    a[pivot], a[left] = a[left], a[pivot]
    i = left + 1
    for j in range(left + 1, right + 1):
        if a[j] < a[left]:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i-1], a[left] = a[left], a[i-1]
    count += right - left
    return i - 1

def find_median(a, first, last):
    middle = first + (last - first) // 2
    if min(a[first], a[last]) < a[middle] < max(a[first], a[last]):
        return middle
    elif min(a[middle], a[last]) < a[first] < max(a[middle], a[last]):
        return first
    else:
        return last

f = open("QuickSort.txt")
lines = f.readlines()
a = [int(line) for line in lines]
global count
count = 0
a_sorted = a.copy()
a_sorted.sort()

a1 = a.copy()
quick_sort(a1, 0, len(a1)-1, "first")
assert a1 == a_sorted
print("First element as pivot: " + repr(count) + " comparisons")

a2 = a.copy()
count = 0
quick_sort(a2, 0, len(a2)-1, "last")
assert a2 == a_sorted
print("Final element as pivot: " + repr(count) + " comparisons")

a3 = a.copy()
count = 0
quick_sort(a3, 0, len(a3)-1, "median")
assert a3 == a_sorted
print("Median element as pivot: " + repr(count) + " comparisons")
