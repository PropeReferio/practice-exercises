from collections import deque

graph_tasks = { "wash the dishes" : ["have lunch"],
                "cook food" : ["have lunch"],
                "have lunch" : [],
                "wash laundry" : ["dry laundry"],
                "dry laundry" : ["fold laundry"],
                "fold laundry" : [] }

def kahn_topsort(graph):
    in_degree = { u : 0 for u in graph } #This block builds a dictionary
    for u in graph:       # with values representing how many uncompleted
        for v in graph[u]: # dependent tasks there are.
            in_degree[v] += 1

    Q = deque() # Double ended queue. Time complexity for popping & appending
    # is O(1). The same operations on a list take O(n)
    for u in in_degree:
        if in_degree[u] == 0:
            Q.appendleft(u)  #Appends to the queue tasks which don't depend on
            #other tasks.

    L = [] #These will contain tasks in order of completion

    while Q:
        u = Q.pop()
        L.append(u) #Adds item from queue to completed tasks list
        for v in graph[u]: #Looks at each task that depends on the completed task
            in_degree[v] -= 1 #and then decrements the uncompleted dependencies
            if in_degree[v] == 0: #If it no longer has dependencies, add it to 
                Q.appendleft(v) # the queue

    if len(L) == len(graph):
        return L #Return the tasks in order of completion.
    else:
        return [] #If there's a cycle, and the tasks can't be completed,
        #return an empty list