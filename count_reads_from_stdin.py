#!/usr/bin/env python

import sys


"""
command:
gzip -cd ${acc}_1.fq.gz | python count_reads_from_gz.py | sed -e 's/Num reads://g' -e 's/Num Bases: //g' |  awk '{print "'$acc'\tclean1\t"$0"\t"$2/$1}' >> Seq_info.clean
"""

i = 0
reads_count = 0
base_count = 0

if not sys.stdin.isatty():
    for line in sys.stdin:
        i += 1
        if i % 4 == 2:
             reads_count += 1
             base_count += len(line.strip())
else:
    sys.exit("This python script will count reads and total bases from stdin data.\n\tFor example:\n\
    \t\tcat x.fastq | python count_reads_from_stdin.py\n\
    \tOr:\n\
    \t\tgzip -cd y.fastq.gz | python count_reads_from_stdin.py")


print "Num reads: " + str(reads_count) + "\tNum Bases: " + str(base_count)

#sfs
