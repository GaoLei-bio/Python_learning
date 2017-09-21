#!/usr/bin/env python

import sys

"""
Convert wrapped fasta lines to ONE lines
python fasta_1_line.py INPUT OUTPUT

"""


INPUT = sys.argv[1]
OUT = sys.argv[2]

input_file= open(INPUT, 'U')
out_file = open(OUT , 'w')

seq = ''

for line in input_file:
    if line[0] == '>' and seq == '':                    # First line of the input file
        header = line                                   # First seq title
    elif line[0] != '>':                                # join the lines of seqs
        seq = seq + line.strip()                        # remove head and tail
    elif line[0] == '>' and seq !='':                   # Second seq
        out_file.write(header + seq + '\n')        # Write it to output; if not, discard it
        seq = ''                                        # empty seq value
        header = line                                   # Get seq title
# last record
out_file.write(header + seq + '\n')

input_file.close()
out_file.close()
