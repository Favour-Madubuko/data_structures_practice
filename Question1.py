#Initialization of the graph using a hashmap
graphs = {
        'A': set(['B','C']),
        'B': set(['C','D','A']),
        'C': set(['B','E','A']),
        'D': set(['B','F','G']),
        'E': set(['C','G']),
        'F': set(['D','G']),
        'G': set(['F','D','E'])
}

# #Question 1
def dfs(graph,start,goal):
    visited ,stack, orderedList=set(),[start], []
    while stack:
        vertex=stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            orderedList.append(vertex)
            stack.extend(graph[vertex]-visited)
            if vertex == goal:
                return orderedList

print(dfs(graphs,'A','G'))