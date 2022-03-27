from Datastructures import Node,Graph
from pagerank import page_rank



Number_of_nodes = int(input("graph size : "))
Nodes_IDs = []
Nodes_Values = []
Nodes = []
for i in range(0,Number_of_nodes):
   Nodes_IDs += [input("Node ID : ")]
   Nodes_Values += [float(input("Node value: "))]
for i in range(0,Number_of_nodes):
    Nodes += [Node(Nodes_IDs[i],Nodes_Values[i])]

Number_of_edges = int(input("number of edges :"))



for i in range(0,Number_of_edges):
   from_node_A = input("from Node ID : ")
   to_node_B = input("to Node ID : ")
   node_A = [Node for Node in Nodes if Node.get_ID() == from_node_A][0]
   node_B = [Node for Node in Nodes if Node.get_ID() == to_node_B][0]
   node_A.add_outgoinglink(node_B)
   node_B.add_incominglink(node_A)

iterations_number = int(input("number of iterations : " ))
damping_factor = float(input("damping factor : " ))

graph = Graph(Nodes)

page_rank(graph,iterations_number,damping_factor)