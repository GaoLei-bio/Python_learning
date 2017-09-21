#!/usr/bin/env python

import sys

INPUT = sys.argv[1]
OUT = sys.argv[2]
MIN = sys.argv[3]
MAX = sys.argv[4]

"""
Command:
python Keep_length_within_a_range.py Input.fa Output.fa Min_length(including) Max_length(excluding) 
"""

input_file= open(INPUT, 'U')
out_file = open(OUT , 'w')

seq = ''

for line in input_file:
    if line[0] == '>' and seq == '':                    # First line of the input file
        header = line                                   # First seq title
    elif line[0] != '>':                                # join the lines of seqs
        seq = seq + line.strip()                        # remove head and tail
    elif line[0] == '>' and seq !='':                   # Second seq
        if len(seq) >= int(MIN) and len(seq) < int(MAX):
            out_file.write(header + seq + '\n')        # Write it to output; if not, discard it
        seq = ''                                        # empty seq value
        header = line                                   # Get seq title
# last record
if len(seq) >= int(MIN) and len(seq) < int(MAX):
    out_file.write(header + seq + '\n')

input_file.close()
out_file.close()
