from Algorithms.graphs_sample import graph, graph_1


def dfs_paths(g, start, goal):
    stack = [(start, [start])]
    while stack:
        vertex, path = stack.pop()
        for i in g[vertex] - set(path):
            if i == goal:
                yield path + [i]
            else:
                stack.append((i, path + [i]))


list(dfs_paths(graph_1, 'A', 'F'))
