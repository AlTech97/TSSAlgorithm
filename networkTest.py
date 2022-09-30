import snap
import TSSAlgorithm as tss

#run the algorithm with a static threshold
def runStaticThreshold():
    graph = snap.LoadEdgeList(snap.TUNGraph, "Dataset/facebook_clean_data/politician_edges.csv", 0, 1, ',')

    for threshold in range(1, 11):
        hash_table = snap.TIntH()

        #Set the static threshold for each node in the hash table
        for node in graph.Nodes():
            hash_table[node.GetId()] = threshold

        seedSet = tss.tssAlgorithm(snap.ConvertGraph(type(graph), graph), hash_table)

        print("t = " + str(threshold) + " - seed set size = " + str(len(seedSet)))

