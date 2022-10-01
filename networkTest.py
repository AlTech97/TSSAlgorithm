import snap
import math
import TSSAlgorithm as tss

#run the algorithm with a static threshold
def runStaticThreshold():
    graph = snap.LoadEdgeList(snap.TUNGraph, "Dataset/facebook_clean_data/politician_edges.csv", 0, 1, ',')

    for threshold in range(1, 16):
        hash_table = snap.TIntH()

        #Set the static threshold for each node in the hash table
        for node in graph.Nodes():
            hashTable[node.GetId()] = threshold

        seedSet = tss.tssAlgorithm(snap.ConvertGraph(type(graph), graph), hashTable)

        print("threshold: " + str(threshold) + "; seed set size: " + str(len(seedSet)))

def runProportionalThreshold():
    # Load Graph
    graph = snap.LoadEdgeList(snap.TUNGraph, "Dataset/facebook_clean_data/politician_edges.csv", 0, 1,',')

    for i in range(16, 1, -1):      # From 10 to 2
        # Set the threshold for each node based on its degree
        hashTable = snap.TIntH()
        proportion = 1/i

        for node in graph.Nodes():
            hashTable[node.GetId()] = math.ceil(proportion * node.GetOutDeg())

        seedSet = tss.tssAlgorithm(snap.ConvertGraph(type(graph), graph), hashTable)
        print("proportion: " + str(proportion) + "; seed set size: " + str(len(seedSet)))