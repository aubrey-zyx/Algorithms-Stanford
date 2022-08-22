from heapq import *


def read_file(filename):
    with open(filename) as f:
        nums = [int(line.split()[0]) for line in f]
    return nums


def get_median(nums):
    medians = []
    heap_low = []     # A max heap representing the smallest half of the array
    heap_high = []    # A min heap representing the largest half of the array
    for x in nums:
        heappush(heap_high, -heappushpop(heap_low, -x))
        if len(heap_high) > len(heap_low):
            heappush(heap_low, -heappop(heap_high))
        medians.append(-heap_low[0])
    return medians


def main():
    nums = read_file("Median.txt")
    medians = get_median(nums)
    print(sum(medians) % 10000)


if __name__ == '__main__':
    main()