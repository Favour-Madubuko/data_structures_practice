#BrREADTH FIRST SEARCH ALGORITHM
graph = {'A':['B','C','E'],
         'B':['A','D','E'],
         'C':['A','F','G'],
         'D':['B'],
         'E':['A','B','D'],
         'F':['C'],
         'G':['C']}
def bfs_connected_component(graph,start):
    #keep track of all visited nodes
    explored = []

    #Keep track of nodes to be checked
    queue = [start]

    #Keep looping until there are nodes still to be checked

    while queue:
        #pop first node from queue
        node = queue.pop(0)
        if node not in explored:
            #Add node
            print("Visited Node",node,"and added it to the list")