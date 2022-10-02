import snap
import math
import random
import copy
import TSSAlgorithm as tss

#run the algorithm with a static threshold
def runStaticThreshold():
    graph = snap.LoadEdgeList(snap.TUNGraph, "Dataset/facebook_clean_data/politician_edges.csv", 0, 1, ',')

    for threshold in range(1, 16):
        hashTable = snap.TIntH()

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

def runProbabilityStaticThreshold():
    # Load Graph
    graph = snap.LoadEdgeList(snap.TUNGraph, "Dataset/facebook_clean_data/politician_edges.csv", 0, 1,',')

    for threshold in range(1, 16):
        # Probability based deferred decision
        # Dictionary with an integer as k and an integer as value
        hashTable = dict()     
        # Dictionary with a string as k and a float as value
        probability = dict()    

        #Set the random probability on edge
        random.seed(123)
        for edge in graph.Edges():
            tupla = edge.GetId()
            k = str(tupla[0]) + "-" + str(tupla[1])
            probability[k] = random.random()

        #set the static threshold
        for node in graph.Nodes():
            hashTable[node.GetId()] = threshold

        mean = 0
        for j in range(1, 16):
            temp = copy.deepcopy(hashTable)
            graph2 = deferredDecision(snap.ConvertGraph(type(graph), graph), probability)
            seedSet= tss.tssAlgorithm(graph2, hashTable)
            size = len(seedSet)
            mean = mean + size
        mean = mean / 15
        print("threshold: " + str(threshold) + "; mean seed set size: " + str(mean))

def deferredDecision(graph, probabilityHashTable):
    for edge in graph.Edges():
        value = random.random()
        tupla = edge.GetId()
        k = str(tupla[0]) + "-" + str(tupla[1])
        # If random number generated is less than edge activation probability
        if value < probabilityHashTable[k]:  
             graph.DelEdge(tupla[0], tupla[1])
    return graph