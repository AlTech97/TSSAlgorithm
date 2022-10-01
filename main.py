from email.mime import base
import networkTest as nt
import snap

basePath = "Dataset/facebook_clean_data/"

if __name__ == "__main__":
    menu = input("TSS test: write one of the following number for make an operation:\n1) run with a static threshold\n2) run with a proportional threshold\n")
    fileName = "politician_edges.csv"
    graph = snap.LoadEdgeList(snap.TUNGraph, basePath + fileName, 0, 1, ',')
    if menu == "1":
        nt.runStaticThreshold(graph)
    elif menu == "2":
        nt.runProportionalThreshold(graph)
    else:
        print("Please choose correct answer")
