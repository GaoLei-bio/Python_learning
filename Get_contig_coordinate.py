#!/usr/bin/env python

import sys

INPUT = sys.argv[1]

"""
command:
python Get_contig_coordinate.py INPUT
# remove ".fa" from input file
"""


input_file = open(INPUT + ".fa", 'U')
out_file = open(INPUT + ".coord", 'w')

seq = ''

start = 0
end = 0

for line in input_file:
    line= line.strip()
    if line[0] == '>' and seq == '':                    # First line of the input file
        header = line.lstrip('>')                                   # First seq title
    elif line[0] != '>':                                # join the lines of seqs
        seq = seq + line.strip()                        # remove head and tail
    elif line[0] == '>' and seq !='':                   # Second seq
        length = len(seq)
        start = end + 1
        end = end + length + 100
        out_file.write(header + "\t" + str(length) + "\t" + INPUT + "\t" + str(start) + "\t" + str(end) + '\n')
        seq = ''                                        # empty seq value
        header = line.lstrip('>')                                   # Get seq title
# last record
length = len(seq)
start = end + 1
end = end + length + 100
out_file.write(header + "\t" + str(length) + "\t" + INPUT + "\t" + str(start) + "\t" + str(end) + '\n')

input_file.close()
out_file.close()
