from email.mime import base
import networkTest as nt
import snap

basePath = "Dataset/facebook_clean_data/"

if __name__ == "__main__":
    menu = input("TSS test: write one of the following number for make an operation:\n1) run with a static threshold\n2) run with a proportional threshold\n3) run with a probability static threshold\n-1)exit")
    while menu != -1:
        fileName = "politician_edges.csv"
        graph = snap.LoadEdgeList(snap.TUNGraph, basePath + fileName, 0, 1, ',')
        if menu == "1":
            nt.runStaticThreshold(graph)
        elif menu == "2":
            nt.runProportionalThreshold(graph)
        elif menu == "3":
            nt.runProbabilityStaticThreshold(graph)
        else:
            print("Please choose correct answer")
        menu = input("TSS test: write one of the following number for make an operation:\n1) run with a static threshold\n2) run with a proportional threshold\n3) run with a probability static threshold\n-1)exit")