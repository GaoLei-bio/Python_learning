#!/usr/bin/env python

import sys

INPUT = sys.argv[1]
OUT = sys.argv[2]

"""
command:
python concatenation.py INPUT OUT
# INPUT and OUT without ".fa"
"""


input_file= open(INPUT + ".fa", 'U')
out_file = open(OUT + ".fa", 'w')

N100 = 'N' * 100

seq = ''

out_file.write(">" + INPUT + "\n")

for line in input_file:
    if line[0] == '>' and seq == '':                    # First line of the input file
        header = line                                   # First seq title
    elif line[0] != '>':                                # join the lines of seqs
        seq = seq + line.strip()                        # remove head and tail
    elif line[0] == '>' and seq !='':                   # Second seq
        out_file.write(seq + N100)        # Write it to output; if not, discard it
        seq = ''                                        # empty seq value
        header = line                                   # Get seq title
# last record
out_file.write(seq + '\n')

input_file.close()
out_file.close()
