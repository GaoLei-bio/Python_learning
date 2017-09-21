#!/usr/bin/env python

import sys

BLOCK = sys.argv[1]
BASE = sys.argv[2]

"""
command:
samtools view sorted_by_reads_name.bam | python Split_sorted_bam_by_number_of_read_pair.py Block_Size Base_out
"""
BLOCK=int(BLOCK)

i=1
Piece = 0
reads_title = ""
pair = []

for line in sys.stdin:
    line = line.strip()
    columns = line.split()

    # if 1st reads of a pair:
    #     output it
    #     i += 1
    # elif 2nd reads of a pair:
    #     ONLY output it
    if columns[0] != reads_title and pair == []:
        # first lines of first pair reads
        if i % BLOCK == 1:
            Piece += 1
        reads_title = columns[0]
        pair.append(line)
        i += 1
    elif columns[0] == reads_title:
        # non-first lines of reads pair
        pair.append(line)
    elif columns[0] != reads_title and pair != []:
        # 2nd, 3rd ...
        with open(BASE + "_part_" + str(Piece) + ".sam", 'a+') as small_file:
            small_file.write("\n".join(pair) + "\n")
        if i % BLOCK == 1:
            Piece += 1
        pair = []
        reads_title = columns[0]
        pair.append(line)
        i += 1

# last pair
with open(BASE + "_part_" + str(Piece) + ".sam", 'a+') as small_file:
    small_file.write("\n".join(pair) + "\n")
