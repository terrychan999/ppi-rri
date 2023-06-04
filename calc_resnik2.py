uniprot_go = open("databases/human_uniprot_go.txt", "r")
uniprot_go_lines = uniprot_go.readlines()
if uniprot_go_lines[0].startswith("Entry"):
    uniprot_go_lines = uniprot_go_lines[1:]
uniprot_go.close()

go_ic_dict = dict()
go_ic = open("databases/human_go_ic.txt", "r")
go_ic_lines = go_ic.readlines()
for line in go_ic_lines:
    line = line.rstrip()
    try:
        go_ic_dict[line.split(" ")[0]] = float(line.split(" ")[1])
    except:
        pass
go_ic.close()

protein_go = dict()
for line in uniprot_go_lines:
    line = line.rstrip()
    try:
        protein_go[line.split("\t")[0]] = line.split("\t")[1].split("; ")
    except:
        pass

for key1 in protein_go.keys():
    for key2 in protein_go.keys():
        if key1 != key2:
            common_go = set(protein_go[key1]).intersection(set(protein_go[key2]))
            if common_go:
                common_go_ic = []
                for go in common_go:
                    try:
                        common_go_ic.append(go_ic_dict[go])
                    except:
                        pass
                try:
                    resnik = max(common_go_ic)
                    print(key1, key2, resnik)
                except:
                    pass