ht = {}


def read_file(filename):
    with open(filename) as f:
        nums = [int(line.split()[0]) for line in f.readlines()]
    for num in nums:
        ht[num] = 1
    return nums


def two_sum(nums, t):
    for x in ht:
        if x != t-x and t-x in ht:
            return True
    return False


def main():
    nums = read_file("2sum.txt")
    count = 0
    for t in range(-10000, 10001):
        if two_sum(nums, t):
            count += 1
    print(count)


if __name__ == "__main__":
    main()