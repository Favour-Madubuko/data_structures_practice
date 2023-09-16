#Question 3
def greedy_best_first_search(graph, start, goal):
    open_set = [(start, 0)]  # Priority queue of nodes to explore, initially containing the start node with a priority of 0.
    closed_set,path = set(),[]  # Set of nodes that have already been explored.

    while open_set:
        current, _ = open_set.pop(0)  # Get the node with the highest priority.

        if current == goal:
            return path  # Goal node reached.

        closed_set.add(current)
        path.append(current)
        # Calculate the cost to reach each neighbor.
        neighbor_costs = [(neighbor, travelcost[current + '-' + neighbor]) for neighbor in graph[current] if neighbor not in closed_set]

        # Sort neighbors based on cost (greedy choice: lowest cost first).
        neighbor_costs.sort(key=lambda x: x[1])

        for neighbor, _ in neighbor_costs:
            if neighbor not in closed_set:
                open_set.insert(0, (neighbor, 0))  # Add neighbor to the open set with a priority of 0.

    return False  # Goal not reached.

travelcost={
     'A-B':1,
     'A-C':4,
     'B-A':1,
     'C-A':4,
     'B-C':2,
     'C-B':2,
     'C-E':5,
     'E-C':5,
     'B-D':3,
     'D-B':3,
     'D-F':2,
     'F-D':2,
     'D-G':4,
     'G-D':4,
     'F-G':1,
     'G-F':1,
     'E-G':3,
     'G-E':3
 }

# travelcost = {
#     'A-B': 1,
#     'A-C': 4,
#     'C-B': 2,
#     'B-C': 2,
#     'C-E': 5,
#     'E-C': 5,
#     'B-D': 3,
#     'D-F': 2,
#     'D-G': 4,
#     'F-G': 1,
#     'E-G': 3,
# }

graph = {
    'A': set(['B', 'C']),
    'B': set(['D', 'C', 'A']),
    'C': set(['A', 'B', 'E']),
    'D': set(['B', 'F', 'G']),
    'E': set(['C', 'G']),
    'F': set(['D', 'G']),
    'G': set(['E', 'D', 'F'])
}
start_node = 'A'
goal_node = 'G'

print(greedy_best_first_search(graph, start_node, goal_node))
#     print('Goal reached: There is a path from {} to {}.'.format(start_node, goal_node))
# else:
#     print('Goal not reached: There is no path from {} to {}.'.format(start_node, goal_node))
