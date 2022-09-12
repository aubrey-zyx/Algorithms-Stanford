import random
from heapq import heapify, heappop, heappush
from collections import defaultdict


def read_file(filename):
    graph = defaultdict(list)
    with open(filename) as f:
        for line in f.readlines()[1:]:
            item = line.split()
            graph[int(item[0])].append([int(item[1]), int(item[2])])
            graph[int(item[1])].append([int(item[0]), int(item[2])])
    return graph


def prim_mst(graph):
    start = random.choice(list(range(1, len(graph) + 1)))
    visited = {start}
    mst = []      # Edges of the MST
    unvisited = []      # Edges & vertices directly connected to X
    for v in graph[start]:
        heappush(unvisited, [v[1], v[0]])
    while len(visited) != len(graph):
        e_star, v_star = heappop(unvisited)
        mst.append(e_star)
        visited.add(v_star)

        # Equal to deleting v_star from heap
        for i, v in enumerate(unvisited):
            if v[1] == v_star:
                v[0] = float('inf')
        heapify(unvisited)

        # Equal to updating the keys of vertices in V-X that are directly connected to v_star
        for w in graph[v_star]:
            if w[0] not in visited:
                heappush(unvisited, [w[1], w[0]])

    return sum(mst)


def main():
    assert prim_mst(G) == 7
    G = read_file("edges.txt")
    print(prim_mst(G))


if __name__ == '__main__':
    main()