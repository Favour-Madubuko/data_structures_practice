import heapq

def Astaralgorithm(graph, start, goal, heuristics):
    visited = set()
    queue = [(heuristics[start], 0, [start])]
    while queue:
        (h, cost, path) = heapq.heappop(queue)
        node = path[-1]
        if node not in visited:
            if node == goal:
                return path
            visited.add(node)
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    g = cost + weight
                    h = heuristics[neighbor]
                    f = g + h
                    heapq.heappush(queue, (f, g, path + [neighbor]))
    return None

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 3)],
    'C': [('E', 5)],
    'D': [('F', 2), ('G', 4)],
    'E': [('G', 3)],
    'F': [('G', 1)],
    'G': [],
}

heuristics = {
    'A': 5,
    'B': 2,
    'C': 4,
    'D': 3,
    'E': 3,
    'F': 1,
    'G': 0,
}

start = 'A'
goal = 'G'
print(Astaralgorithm(graph, start, goal, heuristics))