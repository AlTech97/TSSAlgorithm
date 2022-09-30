import snap

# noinspection PyUnresolvedReferences
def tssAlgorithm(graph: snap.TUNGraph, threshold):
    match = False
    seedSet = set()
    removeSet = set()

    #While the graph is not empty
    while graph.GetNodes() != 0:   
        match = False
        
        #Read all the vertex
        for x in graph.Nodes():
            #case1     
            if threshold[x.GetId()] == 0:
                match = True                
                #print("Case 1: threshold["+str(x.GetId())+"] = 0")
                for y in x.GetOutEdges():
                    if threshold[y] > 0:
                        # reduce the threshold of the neighbor
                        threshold[y] = threshold[y] - 1         
                    removeSet.add(y);

                #remove the edges to the neighbors
                for edge in removeSet:
                    graph.DelEdge(x.GetId(), edge)
                
                #remove the node and clear the removeSet
                graph.DelNode(x.GetId())     
                removeSet.clear()
            #case2
            elif x.GetOutDeg() < threshold[x.GetId()]:
                #print("Case 2: the grade of the node: "+str(x.GetId())+" is: "+str(x.GetOutDeg())+", lower than the threshold[" + str(x.GetId()) + "] = " + str(threshold[x.GetId()]))
                match = True
                seedSet.add(x.GetId())        # Add x to the seed set
            
                for y in x.GetOutEdges():
                    if threshold[y] > 0:
                        threshold[y] = threshold[y] - 1
                    removeSet.add(y)

                for edge in removeSet:
                    graph.DelEdge(x.GetId(), edge)

                graph.DelNode(x.GetId())
                removeSet.clear()
        #case3: if it wasn't find any node to remove
        if not match:     
            argMax = -1
            id = -1
            #select the node that maximize the specified quantity
            for x in graph.Nodes():
                nodeDeg = threshold[x.GetId()]/(x.GetOutDeg() * (x.GetOutDeg() + 1))
                if nodeDeg > argMax:
                    argMax = nodeDeg
                    id = x.GetId()

            #delete the node previosly selected
            node = graph.GetNI(id)
            for y in node.GetOutEdges():
                removeSet.add(y)
            #remove the adiacent edges of the selected node
            for edge in removeSet:
                graph.DelEdge(id, edge)  

            graph.DelNode(id)
            removeSet.clear()
            #print("Case 3: eliminated the node with id: " + str(id))
    return seedSet
