from Bio import SeqIO
import os

# convert fasta to txt

# current directory path
currentPath = os.getcwd()
databasesPath = os.path.join(currentPath, "databases")
proteinFastaName = os.path.join(databasesPath, "uniprot_sprot.fasta.gz")
convertTxtName = os.path.join(databasesPath, "swissProtSeq.txt")

if ".gz" in proteinFastaName:
    import gzip
    handle = gzip.open(proteinFastaName, "rt")
else:
    handle = open(proteinFastaName, "r")
seqRecords = SeqIO.parse(handle, "fasta")

swissProtSeq = open(convertTxtName, "w")
for index, record in enumerate(seqRecords):
    accession_id = record.id.split("|")[1]
    swissProtSeq.write(f"{accession_id} {record.seq}\n")

swissProtSeq.close()
