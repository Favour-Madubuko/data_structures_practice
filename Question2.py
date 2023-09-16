#The Depth-First Search Algorithm to show path from start state to goal state
graphs = {
        'A': set(['B','C']),
        'B': set(['C','D','A']),
        'C': set(['B','E','A']),
        'D': set(['B','F','G']),
        'E': set(['C','G']),
        'F': set(['D','G']),
        'G': set(['F','D','E'])
}
def dfs_paths(graph,start,goal):
    stack = [(start,[start])]

    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path +[next]))

print(list(dfs_paths(graphs,'A','G')))