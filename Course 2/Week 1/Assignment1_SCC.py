import sys
import threading
from collections import defaultdict


class Kosaraju:
    def __init__(self):
        self.t = 0
        self.n = 0
        self.s = None
        self.visited = []
        self.finishing_times = []
        self.leader = defaultdict(list)

    def DFS_loop(self, G, order):
        self.t = 0
        self.s = None
        self.visited = [False] * self.n
        self.finishing_times = [self.n] * self.n
        # self.leader = [v for v in range(1, self.n + 1)]
        for i in order:
            if not self.visited[i-1]:
                self.s = i
                self.DFS(G, i)
        return

    def DFS(self, G, i):
        self.visited[i-1] = True
        #self.leader[i-1] = self.s
        self.leader[self.s].append(i)
        if G[i]:
            for j in G[i]:
                if not self.visited[j-1]:
                    self.DFS(G, j)
        self.t += 1
        self.finishing_times[i-1] = self.t
        return

    def kosaraju(self, G, G_rev):
        self.n = len(G)
        order = [i for i in range(1, self.n + 1)]
        order.reverse()
        self.DFS_loop(G_rev, order)
        for i, val in enumerate(self.finishing_times, 1):
            order[self.n - val] = i
        self.leader.clear()
        self.DFS_loop(G, order)
        return self.leader


def load_graph(filename):
    edges = []
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip().split()
            edges.append((int(line[0]), int(line[1])))
    nodes = list(set([v for edge in edges for v in edge]))
    G = {i: [] for i in range(1, len(nodes) + 1)}
    G_rev = {i: [] for i in range(1, len(nodes) + 1)}
    for edge in edges:
        G[edge[0]].append(edge[1])
        G_rev[edge[1]].append(edge[0])
    return G, G_rev

def main():
    G, G_rev = load_graph("SCC.txt")
    SCCs = Kosaraju().kosaraju(G, G_rev)
    sizes = [len(SCCs[v]) for v in SCCs.keys()]
    sizes_sorted = sorted(sizes, reverse = True) + [0] * 5
    print(','.join(map(str, sizes_sorted[:5])))
    return

if __name__ == '__main__':
    threading.stack_size(67108864)  # 64MB stack
    sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
    thread = threading.Thread(target=main)  # instantiate thread object
    thread.start()  # run program at target