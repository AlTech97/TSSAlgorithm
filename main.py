from email.mime import base
from fileinput import filename
import networkTest as nt
import snap

basePath = "Dataset/facebook_clean_data/"
extension = ".csv"

if __name__ == "__main__":
    fileName = input("Write the name of the dataset\n")
    graph = snap.LoadEdgeList(snap.TUNGraph, basePath + fileName + extension, 0, 1, ',')

    while True:
        menu = input("\nTSS test: write one of the following number for make an operation:\n0) Exit\n1) run with a static threshold\
        \n2) run with a proportional threshold\n3) run with a different probability and static threshold\n4) run with a different probability and proportional threshold\n")
        if menu == "0":
            print("Bye!\n")
            break
        if menu == "1":
            nt.runStaticThreshold(graph)
        elif menu == "2":
            nt.runProportionalThreshold(graph)
        elif menu == "3":
            nt.runProbabilityStaticThreshold(graph)
        elif menu == "4":
            nt.runProbabilityProportionalThreshold(graph)
        else:
            print("Please choose correct answer\n")
