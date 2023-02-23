"""convert fasta to txt"""

from Bio import SeqIO  # requires biopython
import os


currentPath = os.getcwd()  # current directory path
databasesPath = os.path.join(currentPath, "databases")
proteinFastaName = os.path.join(databasesPath, "uniprot_sprot.fasta.gz")
convertTxtName = os.path.join(databasesPath, "uniprotSeq.txt")
seqBasedTxtName = os.path.join(databasesPath, "seqBased.txt")


def load_fasta(fasta_file):  # load fasta directly or with compression
    if fasta_file.endswith(".gz"):
        import gzip
        handle = gzip.open(fasta_file, "rt")
    else:
        handle = open(fasta_file, "r")
    return SeqIO.parse(handle, "fasta")


seqRecords = load_fasta(proteinFastaName)

"""write to txt"""
uniprotSeq = open(convertTxtName, "w")
for index, record in enumerate(seqRecords):
    accession_id = record.id.split("|")[1]
    uniprotSeq.write(f"{accession_id}\t{record.seq}\n")
uniprotSeq.close()

"""write to txt with seq as key"""
# seqBased = open(seqBasedTxtName, "w")
# seqDict = dict()
# for index, record in enumerate(seqRecords):
#     accession_id = record.id.split("|")[1]
#     if record.seq not in seqDict:
#         seqDict[record.seq] = list()
#         seqDict[record.seq].append(accession_id)
#     else:
#         seqDict[record.seq].append(accession_id)
# for seq, accession_ids in seqDict.items():
#     seqBased.write(f"{seq}\t{','.join(accession_ids)}\n")
# seqBased.close()

"""count human proteins"""
# human_count = 0
# for index, record in enumerate(seqRecords):
#     if "_HUMAN" in record.id:
#         human_count += 1
# print(human_count)
