#!/usr/bin/env python
import sys
import gzip

INPUT = sys.argv[1]

"""
command:
python Simplify_fasq_title_python.py INPUT.fastq.gz > OUTPUT.fastq
"""
i = 1

with gzip.open(INPUT,'r') as fin:
    for line in fin:
        if i % 4 == 1:
            columns = line.strip().split()[0].split(".")
            # Get simple title: @ERR1893559.3/1
            print columns[0] + "." + columns[1] + "/" + columns[2]
        if i % 4 == 2:
            print line + "+"
        if i % 4 == 0:
            print line.strip()
        i += 1
