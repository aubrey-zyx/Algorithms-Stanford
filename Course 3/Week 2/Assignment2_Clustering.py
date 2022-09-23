from unionfind import unionfind


def read_file(filename):
    graph = []
    with open(filename) as f:
        lines = f.readlines()
        num_vertices = int(lines[0].split()[0])
        for line in lines[1:]:
            item = list(map(int, line.split()))
            graph.append(item)
    return graph, num_vertices


def clustering(graph, num_vertices, k):
    uf = unionfind(num_vertices)
    graph = sorted(graph, key=lambda x: x[2])
    for item in graph:
        u, v, d = item[0] - 1, item[1] - 1, item[2]
        if not uf.issame(u, v):
            if len(uf.groups()) != k:
                uf.unite(u, v)
            else:
                return d


def main():
    graph, num_vertices = read_file("clustering1_test.txt")
    max_spacing = clustering(graph, num_vertices, 2)
    assert max_spacing == 5
    graph, num_vertices = read_file("clustering1.txt")
    max_spacing = clustering(graph, num_vertices, 4)
    print(max_spacing)


if __name__ == '__main__':
    main()