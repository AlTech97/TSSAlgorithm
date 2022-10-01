import snap
import math
import TSSAlgorithm as tss

#run the algorithm with a static threshold
def runStaticThreshold(graph: snap.TUNGraph):
    for threshold in range(1, 16):
        hashTable = snap.TIntH()
        
        for node in graph.Nodes():
            hashTable[node.GetId()] = threshold
       
        seedSet = tss.tssAlgorithm(snap.ConvertGraph(type(graph), graph), hashTable)

        print("Threshold: " + str(threshold) + "; seed set size: " + str(len(seedSet)))

#run the tss algorithm with a threshold proportional with the degree of each node
def runProportionalThreshold(graph: snap.TUNGraph):
    for i in range(16, 1, -1):
        hashTable = snap.TIntH()
        proportion = 1/i

        for node in graph.Nodes():
            hashTable[node.GetId()] = math.ceil(proportion * node.GetOutDeg())

        seedSet = tss.tssAlgorithm(snap.ConvertGraph(type(graph), graph), hashTable)

        print("Proportion: " + str(proportion) + "; seed set size: " + str(len(seedSet)))
