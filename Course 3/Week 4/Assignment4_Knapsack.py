def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        w, n = int(lines[0].split()[0]), int(lines[0].split()[1])
        values = [int(line.split()[0]) for line in lines[1:]]
        weights = [int(line.split()[1]) for line in lines[1:]]
    return w, n, values, weights


def knapsack(w, n, values, weights):
    v = [[0 for i in range(w + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for x in range(w + 1):
            if x < weights[i - 1]:
                v[i][x] = v[i - 1][x]
            else:
                v[i][x] = max(v[i - 1][x], v[i - 1][x - weights[i - 1]] + values[i - 1])
    return v[n][w]


def main():
    w, n, values, weights = read_file('knapsack1.txt')
    print(knapsack(w, n, values, weights))


if __name__ == '__main__':
    main()