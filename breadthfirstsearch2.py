graph = {'A': ['B', 'C', 'E'],
'B': ['A','D', 'E'],
'C': ['A', 'F', 'G'],
'D': ['B'],
'E': ['A', 'B','D'],
'F': ['C'],
'G': ['C']}

def bfs_connected_component(graph, start):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]
    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
        if node not in explored:
        # add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]
        # add neighbours of node to queue
        for neighbour in neighbours:
            queue.append(neighbour)
    return explored
print(bfs_connected_component(graph,'A'))


# finds shortest path between 2 nodes of a graph using BFS
def bfs_shortest_path(graph, start, goal):
    explored = []
    queue = [[start]]
    if start == goal:
        return "That was easy! Start = goal"
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
        for neighbour in neighbours:
            new_path = list(path)
            new_path.append(neighbour)
            queue.append(new_path)
            if neighbour == goal:
                return new_path
    explored.append(node)
    return "So sorry, but a connecting path doesn't exist :("


bfs_shortest_path(graph, 'G', 'D') # returns ['G', 'C', 'A', 'B', 'D']