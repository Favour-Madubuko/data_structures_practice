graph1 ={'A':set(['B','C']),
        'B':set(['A','D','E']),
        'D':set(['B']),
        'E':set(['B','F']),
        'F':set(['C','E'])
        }

def dfs(graph,start):
    visited ,stack=set(),[start]
    while stack:
        vertex=stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[start]-visited)

    return visited

print(dfs(graph1,'A'))