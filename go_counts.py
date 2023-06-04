uniprot_go = open("databases/ecoli_uniprot_go.txt", "r")
uniprot_go_lines = uniprot_go.readlines()
if uniprot_go_lines[0].startswith("Entry"):
    uniprot_go_lines = uniprot_go_lines[1:]
uniprot_go.close()

go_counts = dict()
for line in uniprot_go_lines:
    line = line.rstrip()
    try:
        go_list = line.split("\t")[1].split("; ")
        for go in go_list:
            if go in go_counts:
                go_counts[go] += 1
            else:
                go_counts[go] = 1
    except:
        pass

human_go_counts = open("databases/ecoli_go_counts.txt", "w")
for go, count in go_counts.items():
    human_go_counts.write(f"{go}\t{count}\n")
human_go_counts.close()