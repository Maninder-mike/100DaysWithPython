from Algorithms.graphs_sample import graph


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


def dfs_1(g, first, visit=None):
    if visit is None:
        visit = set()
    visit.add(first)
    for _ in g[first] - visit:
        dfs_1(g, first, visit)
    return visit


print(dfs_1(graph, "D"))
