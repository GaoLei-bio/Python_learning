import sys
from operator import itemgetter

"""
command:
python sort_seq_reverse.py INPUT.fa OUTPUT.sorted.fa
"""


RAW= sys.argv[1]
SORTED= sys.argv[2]

fasta_file = open(RAW , 'r')
out_file = open(SORTED , 'w')

seq = ''
table = []
for line in fasta_file:
    if line[0] == '>' and seq == '':                    # First line of the input file
        header = line                                   # First seq title
    elif line[0] != '>':                                # join the lines of seqs
        seq = seq + line.strip()                        # remove head and tail
    elif line[0] == '>' and seq !='':                   # Second seq
        row = [header, seq, len(seq)]
        table.append(row)
        seq = ''                                        # empty seq value
        header = line                                   # Get seq title
# last seq
row = [header, seq, len(seq)]
table.append(row)
# using itemgetter
column = 2                                        # cardinal number, Start from 0
table_sorted = sorted(table, key = itemgetter(column), reverse = True)

for row in table_sorted:
    out_put_seq = row[0] + row[1] + "\n"
    out_file.write(out_put_seq)


out_file.close()
fasta_file.close()
