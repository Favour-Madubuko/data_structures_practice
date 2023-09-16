graph1 ={'3M3CL':set(['1M1CR','2CR']),
        '1M1CR':set(['3M2CL']),
        '2CR':set(['3M2CL']),
        '3M2CL':set(['3CR']),
        '3CR':set(['3M1CL']),
        '3M1CL':set(['2M2CR']),
        '2M2CR':set(['2M2CL']),
        '2M2CL':set(['3M1CR']),
        '3M1CR':set(['3CL']),
        '3CL':set(['3M2CR']),
        '3M2CR':set(['2CL']),
        '2CL':set(['3M3CR']),
        '3M3CR':set(['2CL'])
        }

def dfs(graph,start):
    visited ,stack=set(),[start]
    while stack:
        vertex=stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex]-visited)

    return visited

print(dfs(graph1,'3M3CL'))