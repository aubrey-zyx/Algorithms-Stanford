from heapq import *


def read_file(filename):
    nodes = []
    with open(filename) as f:
        lines = f.readlines()
        for i, line in enumerate(lines[1:]):
            nodes.append([int(line.split()[0]), 0, 0])
    return nodes


def huffman_coding(nodes):
    heapify(nodes)
    while len(nodes) > 1:
        u, v = heappop(nodes), heappop(nodes)
        heappush(nodes, [u[0] + v[0], 1 + min(u[1], v[1]), 1 + max(u[2], v[2])])
    return nodes[0][1], nodes[0][2]


def main():
    nodes = read_file("huffman_test.txt")
    assert huffman_coding(nodes) == (2, 3)
    nodes = read_file("huffman.txt")
    print(huffman_coding(nodes))


if __name__ == '__main__':
    main()