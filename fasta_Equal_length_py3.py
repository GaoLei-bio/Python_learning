#!/usr/bin/env python

import sys

"""
Convert wrapped fasta lines to ONE lines
python fasta_Equal_length.py INPUT WIDTH > OUTPUT

"""


INPUT = sys.argv[1]
WIDTH = sys.argv[2]

input_file= open(INPUT)
width = int(WIDTH)

seq = ''

for line in input_file:
    line = line.strip()
    if line.startswith('>') and seq == '':                    # First line of the input file
        header = line                                   # First seq title
    elif not line.startswith('>'):                                # join the lines of seqs
        seq = seq + line.strip()                        # remove head and tail
    elif line.startswith('>') and seq !='':
        # Second seq
        print(header)
        i = 0
        while i < len(seq):
            print(seq[i:i+width])
            i = i + width

        seq = ''                                        # empty seq value
        header = line                                   # Get seq title



# last record
print(header)
i=0
while i < len(seq):
    print(seq[i:i+width])
    i = i + width

input_file.close()
