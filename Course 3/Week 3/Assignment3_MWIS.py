def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        nums = [int(line.split()[0]) for line in lines[1:]]
    return nums


def mwis(nums):
    A = [0] * (len(nums) + 1)
    A[1] = nums[0]
    for i in range(2, len(nums) + 1):
        A[i] = max(A[i - 1], A[i - 2] + nums[i - 1])

    # Reconstruction
    S = []
    i = len(nums)
    while i > 0:
        if A[i - 1] >= A[i - 2] + nums[i - 1]:
            i -= 1
        else:
            S.append(i)
            i -= 2

    return A[-1], S


def main():
    nums = read_file("mwis_test.txt")
    assert mwis(nums) == (15, [4, 1])

    nums = read_file("mwis.txt")
    weight, S = mwis(nums)
    candidates = [1, 2, 3, 4, 17, 117, 517, 997]
    ans = ["1" if i in S else "0" for i in candidates]
    print("".join(ans))


if __name__ == '__main__':
    main()