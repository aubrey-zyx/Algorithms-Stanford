import copy
import math
import random

def contract(graph):
    while len(graph) > 2:
        u = random.choice(list(graph.keys()))      # Randomly pick a remaining edge (u, v)
        v = random.choice(graph[u])
        graph[u].extend(graph[v])      # Merge u and v into a single vertex
        for w in graph[v]:
            graph[w].remove(v)
            graph[w].append(u)
        while u in graph[u]:      # Remove self-loops
            graph[u].remove(u)
        del graph[v]
    cut = len(list(graph.values())[0])
    return cut

def get_min_cut(graph):
    n = len(graph)
    times = int(n ** 2 * math.log(n))
    min_cut = n * (n - 1) / 2
    for i in range(times):
        if i % 1000 == 0:
            print(i)
        G = copy.deepcopy(graph)
        cut = contract(G)
        if cut < min_cut:
            min_cut = cut
            print("Current min cut: " + str(min_cut))
    return min_cut

graph = {}
with open('kargerMinCut.txt') as f:
    for line in f.readlines():
        line = line.strip().split('\t')
        vertices = [int(v) for v in line[1:]]
        graph[int(line[0])] = vertices
print(get_min_cut(graph))