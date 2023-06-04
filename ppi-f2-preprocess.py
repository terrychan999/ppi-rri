"""convert go.obo to txt"""

import os

currentPath = os.getcwd()  # current directory path
databasesPath = os.path.join(currentPath, "databases")
goName = os.path.join(databasesPath, "go.obo")
convertTxtName = os.path.join(databasesPath, "go-directed-graph")
PCFtxtName = os.path.join(databasesPath, "go_term_PFC.txt")


go = open(goName, "r")
goLines = go.readlines()
go.close()
DAG = dict()
PFC = dict()
go_forward = dict() # go_term_path


for line in goLines:
    if line.startswith("[Typedef]"):
        break
    if line.startswith("id:"):
        curr_id = line.split(" ")[1].strip()
        go_forward[curr_id] = list()
        if curr_id not in DAG:
            DAG[curr_id] = list()
    elif line.startswith("namespace:"):
        namespace = line.split(" ")[1].strip()
        if namespace == "biological_process":
            PFC[curr_id] = "P"
        elif namespace == "molecular_function":
            PFC[curr_id] = "F"
        elif namespace == "cellular_component":
            PFC[curr_id] = "C"
    elif line.startswith("is_a:"):
        is_a = line.split(" ")[1].strip()
        go_forward[curr_id].append(is_a)
        if is_a not in DAG:
            DAG[is_a] = list()
            DAG[is_a].append(curr_id)
        else:
            if curr_id not in DAG[is_a]:
                DAG[is_a].append(curr_id)
    elif line.startswith("relationship: part_of") or line.startswith("intersection_of: part_of"):
        part_of = line.split(" ")[2].strip()
        # go_forward[curr_id].append(part_of) # ??part_of is not ancestor??
        if part_of not in DAG:
            DAG[part_of] = list()
            DAG[part_of].append(curr_id)
        else:
            if curr_id not in DAG[part_of]:
                DAG[part_of].append(curr_id)
    elif line.startswith("relationship: regulates") or line.startswith("intersection_of: regulates"):
        regulates = line.split(" ")[2].strip()
        go_forward[curr_id].append(regulates)


# """write to txt"""
# directedGraph = open(convertTxtName, "w")
# for key, value in DAG.items():
#     directedGraph.write(f"{key}\t{' '.join(value)}\n")
# directedGraph.close()

# go_term_PFC = open(PCFtxtName, "w")
# for key, value in PFC.items():
#     go_term_PFC.write(f"{key},{value}\n")
# go_term_PFC.close()
