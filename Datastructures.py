
class Node :

     def __init__(self,ID,value):
         self.__ID = ID
         self.__value = value 
         self.__outgoing_edges = []
         self.__incoming_edges = []
     
     def add_outgoinglink(self,target): 
         self.__outgoing_edges = self.__outgoing_edges + [target]
    
     def add_incominglink(self,target):
         self.__incoming_edges = self.__incoming_edges + [target]
     def set_value(self,value):
         self.__value = value
     def get_value(self):
         return self.__value
     def get_ID(self):
         return self.__ID
     def get__outgoinglink(self):
         return self.__outgoing_edges
     def get__incominglinks(self):
         return self.__incoming_edges

class Graph :
    
    
    __Nodes = []

    def __init__(self,Nodes):
        self.__Nodes = Nodes
    def look_for(self,Node_ID):
        for node in self.__Nodes:
            if node.get_ID() == Node_ID:
                return node
    def get_Nodes(self):
        return self.__Nodes

    def look_for_IDs(self):
        IDs = []
        for node in self.__Nodes:
            IDs = IDs + node.get_ID()
        return IDs
    
    def set_values(self,dictionairy):
        for x in dictionairy.keys():
            (self.look_for(x)).set_value(dictionairy[x])

    def page_rank_nodes(self) :
        ranked_nodes = sorted(self.__Nodes, key=lambda x: x.get_value(),reverse=True)
        return ranked_nodes

    
        



    

        