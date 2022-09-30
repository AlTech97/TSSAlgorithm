import snap


# noinspection PyUnresolvedReferences
def tss(graph: snap.TUNGraph, threshold):

    match = False
    s = set()
    removeSet = set()

    while graph.GetNodes() != 0:   # Finché non è vuoto il grafo
        match = False

        for x in graph.Nodes():     # Scorrere i vertici
            if threshold[x.GetId()] == 0:
                match = True                
                print("Caso 1: threshold["+str(x.GetId())+"] = 0")
                for y in x.GetOutEdges():
                    if threshold[y] > 0:
                        threshold[y] = threshold[y] - 1         # Si riduce il threshold dei vicini
                    removeSet.add(y);

                for edge in removeSet:
                    graph.DelEdge(x.GetId(), edge)     # Si rimuovono gli archi con i vicini.

                graph.DelNode(x.GetId())            # Si rimuove il nodo.
                removeSet.clear()
            elif x.GetOutDeg() < threshold[x.GetId()]:
                print("Caso 2: grado di "+str(x.GetId())+" pari a "+str(x.GetOutDeg())+" e minore di threshold[" + str(x.GetId()) + "] = " + str(threshold[x.GetId()]))
                match = True
                s.add(x.GetId())        # Aggiunto x al seed set
                
                for y in x.GetOutEdges():   # Rimozione del nodo dal grafo
                    if threshold[y] > 0:
                        threshold[y] = threshold[y] - 1
                    removeSet.add(y)

                for edge in removeSet:
                    graph.DelEdge(x.GetId(), edge)  # Si rimuovono gli archi con i vicini.

                graph.DelNode(x.GetId())
                removeSet.clear()


        if not match:      # Se non è stato trovato un nodo da rimuovere per il threshold
            argMax = -1
            id = -1
            for x in graph.Nodes():     # Selezione del nodo che massimizza la quantità specificata
                nodeDeg = threshold[x.GetId()]/(x.GetOutDeg() * (x.GetOutDeg() + 1))
                if nodeDeg > argMax:
                    argMax = nodeDeg
                    id = x.GetId()

            # Eliminare il nodo che massimizza la quantità
            node = graph.GetNI(id)
            for y in node.GetOutEdges():  # Rimozione del nodo dal grafo
                removeSet.add(y)

            for edge in removeSet:
                graph.DelEdge(id, edge)  # Si rimuovono gli archi con i vicini.

            graph.DelNode(id)
            removeSet.clear()
            print("Caso 3: eliminato nodo " + str(id))

    return s



'''
g1 = snap.TUNGraph.New()
g1.AddNode(0)
g1.AddNode(1)
g1.AddNode(2)
g1.AddNode(3)
g1.AddEdge(0, 1)
g1.AddEdge(1, 2)
g1.AddEdge(2, 3)
threshold = snap.TIntH()
for x in g1.Nodes():
    threshold[x.GetId()] = 2
    print("threshold di " + str(x.GetId()) + " pari a " + str(threshold[x.GetId()]))
s = tss(snap.ConvertGraph(type(g1), g1), threshold)
for id in s:
    print("Nodo: " + str(id))
'''