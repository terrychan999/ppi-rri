"""convert fasta to txt"""

from Bio import SeqIO  # requires biopython
import os


currentPath = os.getcwd()  # current directory path
databasesPath = os.path.join(currentPath, "databases")
proteinFastaName = os.path.join(databasesPath, "uniprot_sprot.fasta.gz")
convertTxtName = os.path.join(databasesPath, "uniprotSeq.txt")


def load_fasta(fasta_file):  # load fasta directly or with compression
    if ".gz" in fasta_file:
        import gzip
        handle = gzip.open(fasta_file, "rt")
    else:
        handle = open(fasta_file, "r")
    return SeqIO.parse(handle, "fasta")


seqRecords = load_fasta(proteinFastaName)

# write to txt
uniprotSeq = open(convertTxtName, "w")
for index, record in enumerate(seqRecords):
    accession_id = record.id.split("|")[1]
    uniprotSeq.write(f"{accession_id}\t{record.seq}\n")
uniprotSeq.close()
