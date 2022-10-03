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

        targetSet = tss.tssAlgorithm(snap.ConvertGraph(type(graph), graph), hashTable)

        print("Threshold: " + str(threshold) + "; Target Set size: " + str(len(targetSet)))

#run the tss algorithm with a threshold proportional with the degree of each node
def runProportionalThreshold(graph: snap.TUNGraph):
    for i in range(MAX_RANGE, MIN_RANGE, -1):
        hashTable = snap.TIntH()
        proportion = 1/i

        for node in graph.Nodes():
            hashTable[node.GetId()] = math.ceil(proportion * node.GetOutDeg())

        targetSet = tss.tssAlgorithm(snap.ConvertGraph(type(graph), graph), hashTable)

        print("Proportion: " + str(proportion) + "; Target Set size: " + str(len(targetSet)))

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
            targetSet= tss.tssAlgorithm(tempGraph, hashTable)
            size = len(targetSet)
            sum = sum + size
        mean = sum / (MAX_RANGE-1)

        print("Threshold: " + str(threshold) + "; Mean Target Set size: " + str(mean))

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
        for j in range(MIN_RANGE, 3):
            threshold = copy.deepcopy(hashTable)
            tempGraph = deferredDecision(snap.ConvertGraph(type(graph), graph), edgesProbability)
            targetSet = tss.tssAlgorithm(tempGraph, threshold)
            size = len(targetSet)
            sum = sum + size
        mean = sum / (MAX_RANGE - 1)
        
        print("Proportion: " + str(proportion) + "; Mean Target Set size: " + str(mean))
