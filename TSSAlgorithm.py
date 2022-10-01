import snap

# noinspection PyUnresolvedReferences
def tssAlgorithm(graph: snap.TUNGraph, threshold):
    seedSet = set()
    removeSet = set()
    
    #While the graph is not empty
    while graph.GetNodes() != 0:   
        match = False
        
        #Read all the vertex
        for node in graph.Nodes():
            #case1     
            if threshold[node.GetId()] == 0:
                match = True                
                for neighbor in node.GetOutEdges():
                    if threshold[neighbor] > 0:
                        # reduce the threshold of the neighbor
                        threshold[neighbor] = threshold[neighbor] - 1         
                    removeSet.add(neighbor);

                #remove the edges to the neighbors
                for edge in removeSet:
                    graph.DelEdge(node.GetId(), edge)
                
                #remove the node and clear the removeSet
                graph.DelNode(node.GetId())     
                removeSet.clear()
            #case2
            elif node.GetOutDeg() < threshold[node.GetId()]:
                match = True
                seedSet.add(node.GetId())        # Add node to the seed set
            
                for neighbor in node.GetOutEdges():
                    if threshold[neighbor] > 0:
                        threshold[neighbor] = threshold[neighbor] - 1
                    removeSet.add(neighbor)

                for edge in removeSet:
                    graph.DelEdge(node.GetId(), edge)

                graph.DelNode(node.GetId())
                removeSet.clear()
        #case3: if it wasn't find any node to remove
        if not match:     
            argMax = -1
            id = -1
            #select the node that maximize the specified quantity
            for node in graph.Nodes():
                nodeDeg = threshold[node.GetId()]/(node.GetOutDeg() * (node.GetOutDeg() + 1))
                if nodeDeg > argMax:
                    argMax = nodeDeg
                    id = node.GetId()

            #delete the node previosly selected
            node = graph.GetNI(id)
            for neighbor in node.GetOutEdges():
                removeSet.add(neighbor)
            #remove the adiacent edges of the selected node
            for edge in removeSet:
                graph.DelEdge(id, edge)  

            graph.DelNode(id)
            removeSet.clear()

    return seedSet
