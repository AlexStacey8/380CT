def BFS(graph,startVertex):
    listOfNodes = list(graph.nodes())
    #created the list that the functiopn must create for DHC to be true
    finalList = listOfNodes + [startVertex]
    print(finalList)
    queue = []
    visited = []
    queue.insert(0,startVertex) #append the vertex to the queue
    #if startNode has no edges driected to another node or no edges at all then return false
    possible = False
    for edge in list(graph.edges):
        if edge == (startVertex,startVertex):
            continue
        elif edge[1] == startVertex:
            possible = True
        else:
            continue
    if possible == False:
        return(False)
    else:
        lengthOfEdgeList = len(list(graph.edges(startVertex)))
        print("Edges of Start >> " + str(lengthOfEdgeList))
        edgesListOfStartNode = list(graph.edges(startVertex))
        if lengthOfEdgeList == 0 or (edgesListOfStartNode == [(startVertex,startVertex)]):
            return(False)
        else:
            startNodeC = 0
            while queue != []:
                #if the start node is visted more than 2 times then we return false
                u = queue.pop()
                print("popped >> " + str(u))
                print("Visited Prior to checking for final condition >> " + str(visited))
                if set(visited) == set(finalList) and (visited[-1] == startVertex):
                    return(True)
                else:
                    if u not in visited or u == startVertex:
                        if u == startVertex:
                            startNodeC = startNodeC + 1
                        if startNodeC > 2:
                            return(False)
                            break
                        visited.append(u)
                        print("Visited >> " + str(visited))
                        print("Edges to go to >> " + str([i[1] for i in list(graph.edges(u))]))
                        for edge in list(graph.edges(u)):
                            queue.insert(0,edge[1])
                print("Queue >>" + str(queue))

    return(False)
def DFS(graph,startVertex):
    listOfNodes = list(graph.nodes())
    #created the list that the functiopn must create for DHC to be true
    finalList = listOfNodes + [startVertex]
    print(finalList)
    stack = []
    visited = []
    stack.append(startVertex)
    #if the start vertex has no edges coming into it from other nodes then a hamiltonian cycle isnt possible
    possible = False
    for edge in list(graph.edges):
        if edge == (startVertex,startVertex):
            continue
        elif edge[1] == startVertex:
            possible = True
        else:
            continue
    if possible == False:
        return(False)
    else:
        #if startNode has no edges driected to another node or no edges at all then return false
        lengthOfEdgeList = len(list(graph.edges(startVertex)))
        print("Edges of Start >> " + str(lengthOfEdgeList))
        edgesListOfStartNode = list(graph.edges(startVertex))
        if lengthOfEdgeList == 0 or (edgesListOfStartNode == [(startVertex,startVertex)]):
            return(False)
        else:
            startNodeC = 0
            while stack != []:
                #if the start node is visted more than 2 times then we return false
                u = stack.pop()
                print("popped >> " + str(u))
                print("Visited Prior to checking for final condition >> " + str(visited))
                if set(visited) == set(finalList) and (visited[-1] == startVertex):
                    return(True)
                else:
                    if u not in visited or u == startVertex:
                        if u == startVertex:
                            startNodeC = startNodeC + 1
                        if startNodeC > 2:
                            return(False)
                            break
                        visited.append(u)
                        print("Visited >> " + str(visited))
                        print("Edges to go to >> " + str([i[1] for i in list(graph.edges(u))]))
                        for edge in list(graph.edges(u)):
                            stack.append(edge[1])
                print("stack >>" + str(stack))

        return(False)
    
def exhaustiveSearch(graph,startNode):
    print("---<DFS>---")
    dfs = DFS(graph,startNode)
    print("---<BFS>---")
    bfs = BFS(graph,startNode)
    if dfs == True or bfs == True:
        return(True)
    else:
        return(False)
                        
graphTest = createRandomGraph()
displayGraphInfo(graphTest)
exhaustiveSearch(graphTest,1)
