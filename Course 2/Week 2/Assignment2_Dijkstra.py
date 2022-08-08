def load_graph(filename):
    graph = []
    with open(filename) as f:
        for line in f.readlines():
            graph.append([])
            data = line.split()
            v = int(data[0]) - 1
            for i in range(1, len(data)):
                cur = data[i].split(',')
                w = int(cur[0]) - 1
                edge_length = int(cur[1])
                graph[v].append((w, edge_length))
    return graph

def dijkstra(G, source):
    n = len(G)
    visited = []
    visited.append(source)
    A = [100000] * n
    A[source] = 0
    B = [[]] * n
    while len(visited) < n:
        min_edge = 100000
        distances = {}     # Lengths of edges crossing the frontier
        for v in visited:
            for w_info in G[v]:
                w = w_info[0]
                l = w_info[1]
                if w not in visited:
                    distances[(v, w)] = A[v] + l
        (v_star, w_star), dist = min(distances.items(), key=lambda x: x[1])
        visited.append(w_star)
        A[w_star] = dist
    return A

G = load_graph("dijkstraData.txt")
source = 1
vertices = [7,37,59,82,99,115,133,165,188,197]
A = dijkstra(G, source-1)
res = []
for i in range(len(vertices)):
    res.append(A[vertices[i] - 1])
print(','.join(map(str, res)))