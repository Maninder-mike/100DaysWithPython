graph = {'A': {'B', 'C'},
         'B': {'A', 'C', 'D'},
         'C': {'B'},
         'D': {'A', 'C'},
         'E': {'B', 'D'},
         'F': {'B', 'E'},
         'G': {'D', 'E'}}

graph_1 = {'A': set(['B', 'C']),
           'B': set(['A', 'D', 'E']),
           'C': set(['A', 'F']),
           'D': set(['B']),
           'E': set(['B', 'F']),
           'F': set(['C', 'E'])}


def dfs_paths(g, start, goal):
    stack = [(start, [start])]
    while stack:
        vertex, path = stack.pop()
        for i in g[vertex] - set(path):
            if i == goal:
                yield path + [i]
            else:
                stack.append((i, path + [i]))


print(list(dfs_paths(graph_1, 'A', 'F')))
