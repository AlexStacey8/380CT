#module for building the graphs
import networkx as nx
#displaying the graph module
import matplotlib.pyplot as plt
%matplotlib inline
import random

#create the graph
graph = nx.DiGraph()

#adding nodes to the graph
graph.add_node(1)
#add multiple nodes using add_from and the variable has to be iterable
graph.add_nodes_from(range(2,6)) #adds nodes 2,3,4,5
#removing nodes
#graph.remove_node(node)
#removing multiple
#graph.remove_nodes_from(listOfNodes)

#adding/removing edges
#graph.add_edge(1,2) #two arguments are the nodes you want to connect edge will go from 1 -> 2
#graph.remove_edge(node1,node2)
graph.add_edges_from([(1,2),(1,4),(1,3),(1,5),(2,5),(3,4),(3,5),(3,1),(4,4),(4,1),(4,3),(5,1),(5,4),(5,6),(5,2),(6,4),(6,6)]) #list of tuples
#graph.remove_edges_from()

#drawing graph
nx.draw_circular(graph, with_labels=True)
print("---<Graph Information>---")
print(nx.info(graph))
print("N.B. Although not shown on the graph there is an edge going from node 1 to node 1")
#displying graph
plt.draw()
plt.show()
