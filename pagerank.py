from Datastructures import Node, Graph


def page_rank(Graph,iterations_number,damping_factor = 1):
    Nodes = Graph.get_Nodes()
    for i in range(0,iterations_number):
        update_dictionary = {}
        for node in Nodes:
            incoming_nodes = node.get__incominglinks()
            future_value = 0
            for incoming_node in incoming_nodes:
                future_value = future_value + (incoming_node.get_value())/len(incoming_node.get__outgoinglink())
            future_value = damping_factor *future_value
            future_value += (1-damping_factor)/len(Nodes)
            update_dictionary[node.get_ID()] = future_value
        Graph.set_values(update_dictionary)
    ranked_nodes = Graph.page_rank_nodes()
    for k in range(0,len(ranked_nodes)):
        print("Rank ",k+1,"Node ID",ranked_nodes[k].get_ID(),"Node page rank :",ranked_nodes[k].get_value(),"\n")
    
        


