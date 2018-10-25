#!/usr/bin/env python

import sys
import gzip


"""
command:
python count_reads_from_fq.py ${acc}_1.fastq | sed -e 's/Num reads://g' -e 's/Num Bases: //g' |  awk '{print "'$acc'\tde_dup1\t"$0"\t"$2/$1}' >> Seq_info.clean
"""

if len(sys.argv) < 2:
    sys.exit("One read per four lines\n\tusage:\n\t\tpython count_reads.py input.fastq\n\tor:\n\t\tpython count_reads.py input.fastq.gz\n\tOutput:\n\t\tNum reads: xxx\tNum Bases: yyy")

FQ = sys.argv[1]

i = 0
reads_count = 0
base_count = 0

# open reads file
if FQ.endswith(".gz"):
    input_file = gzip.open(FQ, 'rb')
else:
    input_file = open(FQ)

# count
for line in input_file:
    i += 1
    if i % 4 == 2:
         reads_count += 1
         base_count += len(line.strip())

# close reads file
input_file.close()

# print output
print "Num reads: " + str(reads_count) + "\tNum Bases: " + str(base_count)

#sfs
