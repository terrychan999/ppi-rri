"""convert go.obo to txt"""

import os

currentPath = os.getcwd()  # current directory path
databasesPath = os.path.join(currentPath, "databases")
goName = os.path.join(databasesPath, "go.obo")
convertTxtName = os.path.join(databasesPath, "go-directed-graph")

go = open(goName, "r")
goLines = go.readlines()
go.close()
DAG = dict()

for line in goLines:
    if "GO:" in line:
        if line.startswith("id:"):
            curr_id = line.split(" ")[1].strip()
            if curr_id not in DAG:
                DAG[curr_id] = list()
        elif line.startswith("is_a:"):
            is_a = line.split(" ")[1].strip()
            if is_a not in DAG:
                DAG[is_a] = list()
                DAG[is_a].append(curr_id)
            else:
                if curr_id not in DAG[is_a]:
                    DAG[is_a].append(curr_id)
        elif line.startswith("relationship: part_of") or line.startswith("intersection_of: part_of"):
            part_of = line.split(" ")[2].strip()
            if part_of not in DAG:
                DAG[part_of] = list()
                DAG[part_of].append(curr_id)
            else:
                if curr_id not in DAG[part_of]:
                    DAG[part_of].append(curr_id)

"""write to txt"""
directedGraph = open(convertTxtName, "w")
for key, value in DAG.items():
    directedGraph.write(f"{key}\t{' '.join(value)}\n")
directedGraph.close()
