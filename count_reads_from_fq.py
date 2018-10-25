#!/usr/bin/env python

import sys

FQ = sys.argv[1]
"""
command:
python count_reads_from_fq.py ${acc}_1.fastq | sed -e 's/Num reads://g' -e 's/Num Bases: //g' |  awk '{print "'$acc'\tde_dup1\t"$0"\t"$2/$1}' >> Seq_info.clean
"""

i = 0
reads_count = 0
base_count = 0

with open(FQ) as input_file:
    for line in input_file:
        i += 1
        if i % 4 == 2:
             reads_count += 1
             base_count += len(line.strip())

print "Num reads: " + str(reads_count) + "\tNum Bases: " + str(base_count)

#sfs
