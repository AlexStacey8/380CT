#Vertex Graph
class Vertex:
    def __init__(self,label):

        self.label = label
        self.edges = []

        self.edgesList = [] # for printing so i can confirm it works

    def getInfo(self):
        print("Vertex >> " + str(self.label) + "\nEdges >> " + str(self.edgesList))

    def addEdge(self,vertex2):
        if vertex2 in self.edges:
            pass
        else:
            (self.edges).append(vertex2)
            (self.edgesList).append(vertex2.label)

            (vertex2.edges).append(self)
            (vertex2.edgesList).append(self.label)

        
    

class Graph:
    def __init__(self):
        self.vertices = []
        self.verticesList = [] #I append labels to this for printing
        self.numberOfVertices = 0

    def addVertex(self,vertex):
        self.numberOfVertices = self.numberOfVertices + 1
        
        v = Vertex(vertex)
        (self.vertices).append(v)
        (self.verticesList).append(v.label)

        return(v)
        
    def getVertices(self):
        print(self.verticesList)
        
    def getNumberOfVertices(self):
        print(self.numberOfVertices)

    def depthFirstSearch(self,startVertex):
        
        stack = []
        visited = []

        stack.append(startVertex)

        while stack != []:
            u = stack.pop()
            if u.label not in visited:
                visited.append(u.label)
                for edge in u.edges:
                    stack.append(edge)

        return(visited)
    
        f = open("DFS.txt","w")
        f.write("Depth First Traversal >> " + str(visited))
        f.close()





    def breadthFirstSearch(graph,startVertex):
        queue = []
        visited = []

        queue.insert(0,startVertex)

        while queue != []:
            u = queue.pop()

            if u.label not in visited:
                visited.append(u.label)

                for edge in u.edges:
                    queue.insert(0,edge)

        return(visited)
        
        f = open("BFS.txt","w")
        f.write("Breadth First Traversal >> " + str(visited))
        f.close()


graph = Graph()
v1 = graph.addVertex(6)
v2 = graph.addVertex(5)
v3 = graph.addVertex(4)
v4 = graph.addVertex(3)
v5 = graph.addVertex(2)


v1.addEdge(v2)
v1.addEdge(v3)
v1.addEdge(v2)

v2.addEdge(v4)

v3.addEdge(v4)

v4.addEdge(v5)

v1.getInfo()
v2.getInfo()
v3.getInfo()
v4.getInfo()
v5.getInfo()

print(graph.depthFirstSearch(v3))

print(graph.breadthFirstSearch(v3))




        
        
