def dfs (graph,start):
    graph = {
        'A': set(['B','C']),
        'B': set(['A','D','E']),
        'C': set([]),
        'D': set([]),
        'E': set(['B','F']),
        'F': set(['C','E'])
    }