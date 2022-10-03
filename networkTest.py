import snap
import math
import random
import copy
import TSSAlgorithm as tss

MIN_RANGE = 1
MAX_RANGE = 16

#run the algorithm with a static threshold
def runStaticThreshold(graph: snap.TUNGraph):
    for threshold in range(MIN_RANGE, MAX_RANGE):
        hashTable = snap.TIntH()

        #Set the static threshold for each node in the hash table
        for node in graph.Nodes():
            hashTable[node.GetId()] = threshold

        seedSet = tss.tssAlgorithm(snap.ConvertGraph(type(graph), graph), hashTable)

        print("Threshold: " + str(threshold) + "; seed set size: " + str(len(seedSet)))

#run the tss algorithm with a threshold proportional with the degree of each node
def runProportionalThreshold(graph: snap.TUNGraph):
    for i in range(MAX_RANGE, MIN_RANGE, -1):
        hashTable = snap.TIntH()
        proportion = 1/i

        for node in graph.Nodes():
            hashTable[node.GetId()] = math.ceil(proportion * node.GetOutDeg())

        seedSet = tss.tssAlgorithm(snap.ConvertGraph(type(graph), graph), hashTable)
        print("Proportion: " + str(proportion) + "; seed set size: " + str(len(seedSet)))

def deferredDecision(graph, probabilityHashTable):
    for edge in graph.Edges():
        value = random.random()
        tupla = edge.GetId()
        id = str(tupla[0]) + "," + str(tupla[1])
        # If random number generated is less than edge activation probability
        if value < probabilityHashTable[id]:  
             graph.DelEdge(tupla[0], tupla[1])
    return graph

#Run a static-threshold tss with a random probability of the edge
def runProbabilityStaticThreshold(graph: snap.TUNGraph):
    for threshold in range(MIN_RANGE, MAX_RANGE):
        hashTable = dict()     
        edgesProbability = dict()    

        #Set a random probability on every edge
        random.seed(123)
        for edge in graph.Edges():
            tupla = edge.GetId()
            id = str(tupla[0]) + "," + str(tupla[1])
            edgesProbability[id] = random.random()

        #set the static threshold
        for node in graph.Nodes():
            hashTable[node.GetId()] = threshold

        mean = 0
        sum = 0
        for i in range(MIN_RANGE, MAX_RANGE):
            tempGraph = deferredDecision(snap.ConvertGraph(type(graph), graph), edgesProbability)
            seedSet= tss.tssAlgorithm(tempGraph, hashTable)
            size = len(seedSet)
            sum = sum + size
        mean = sum / (MAX_RANGE-1)
        print("threshold: " + str(threshold) + "; mean seed set size: " + str(mean))

#Run a proportional-threshold tss with a random edgesProbability of the edge
def runProbabilityProportionalThreshold(graph: snap.TUNGraph):
    for i in range(MAX_RANGE, MIN_RANGE, -1): 
        hashTable = dict()              
        edgesProbability = dict()       

        #Set a random probability on every edge
        random.seed(123)
        for edge in graph.Edges():
            tupla = edge.GetId()
            id = str(tupla[0]) + "," + str(tupla[1])
            edgesProbability[id] = random.random()

        #Set the degree based threshold for every node
        proportion = 1/i
        for node in graph.Nodes():
            hashTable[node.GetId()] = math.ceil(proportion * node.GetOutDeg())
            
        mean = 0
        sum = 0
        for j in range(MIN_RANGE, MAX_RANGE):
            threshold = copy.deepcopy(hashTable)
            tempGraph = deferredDecision(snap.ConvertGraph(type(graph), graph), edgesProbability)
            seedSet = tss.tssAlgorithm(tempGraph, threshold)
            size = len(seedSet)
            sum = sum + size
        mean = sum / (MAX_RANGE - 1)
        print("proportion: " + str(proportion) + "; mean seed set size: " + str(mean))