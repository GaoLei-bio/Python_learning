from Bio import SeqIO
from Bio.Seq import Seq
import sys

"""
command:
python test.fa codon_pos1.fa codon_pos2.fa codon_pos3.fa
"""

FASTA = sys.argv[1]
CODON1 = sys.argv[2]
CODON2 = sys.argv[3]
CODON3 = sys.argv[4]

fasta_file = open(FASTA, "r")
codon1 = open(CODON1, 'w')
codon2 = open(CODON2, 'w')
codon3 = open(CODON3, 'w')

for seq_record in SeqIO.parse(fasta_file, "fasta"):
    pos1 = seq_record.seq[0::3]
    pos2 = seq_record.seq[1::3]
    pos3 = seq_record.seq[2::3]

    codon1.write(">" + seq_record.id + "_1\n" + str(pos1) + "\n")
    codon2.write(">" + seq_record.id + "_2\n" + str(pos2) + "\n")
    codon3.write(">" + seq_record.id + "_3\n" + str(pos3) + "\n")

fasta_file.close()
codon1.close()
codon2.close()
codon3.close()
