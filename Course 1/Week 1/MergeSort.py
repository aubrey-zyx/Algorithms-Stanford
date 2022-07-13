def merge_sort(a, left, right):
    if left < right:
        mid = int((left + right) // 2)
        merge_sort(a, left, mid)
        merge_sort(a, mid+1, right)
        merge(a, left, mid, right)


def merge(a, left, mid, right):
    i = left
    j = mid + 1
    tmp = []
    while i <= mid and j <= right:
        if a[i] <= a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1
    if i <= mid:
        tmp.extend(a[i:mid+1])
    if j <= right:
        tmp.extend(a[j:right+1])
    a[left:right+1] = tmp


a = [6,1,51,24,888,25,72,5,90,134]
merge_sort(a, 0, len(a)-1)
print(a)