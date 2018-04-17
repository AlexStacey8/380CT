def createRandomGraph():
    #create graph
    graph = nx.DiGraph()
    #create the 6 nodes
    graph.add_nodes_from(range(1,7))
    #get a random number between 6 and 18 to be the total numebr of edges
    totalNumOfEdges = random.randint(6,18)
    #every node has to have an edge so this loop adds one edge to each node
    for i in range(1,7):
        #add node to the graph 
        graph.add_edge(i,random.randint(1,6))
    #now we will generate random edge with the remaining edges if there are any
    edgesRemaining = totalNumOfEdges - 6
    while edgesRemaining >= 1:
        startNode = int(random.randint(1,6))
        endNode = int(random.randint(1,6))
        #see if edge is alredy in the graph
        edge = (startNode,endNode)
        if edge in list(graph.edges()):
            edgesRemaining = edgesRemaining - 1
        else:
            graph.add_edge(startNode,endNode)
            edgesRemaining = edgesRemaining - 1
        
    return(graph)

def displayGraphInfo(graph):
    #drawing graph
    nx.draw_circular(graph, with_labels=True)
    #displying graph
    plt.draw()
    plt.show()
    #getting graph info
    print(nx.info(graph))
    #prints out the edges within the graph
    edgesList = graph.edges()
    for i in graph.edges():
        print(str(i[0]) + " --> " + str(i[1]))

graph = createRandomGraph()
displayGraphInfo(graph)
