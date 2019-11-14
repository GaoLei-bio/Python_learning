#!/usr/bin/env python

import sys
import pysam

'''
python pysam_get_base_on_pos.py Bam chr pos MAPQ > OUTPUT

e.g.
python pysam_get_base_on_pos.py B.bam OXv7ch01 1344887 30 > OUTPUT

Output:
Chr         Pos     Depth   A       T       C       G
OXv7ch01    1344887 19      13      0       0       6

Get bases on a given pos.
Set Min MAPQ

'''
Bam = sys.argv[1]
Chr = sys.argv[2]
Pos = int(sys.argv[3]) - 1
MAPQ = int(sys.argv[4])

bf = pysam.AlignmentFile(Bam, "rb" )

# creat empty count dict
Bases = ["A","T","C","G"]
base_count = {}
for b in Bases:
    base_count[b] = 0

Total = 0

with pysam.AlignmentFile(Bam, "rb" ) as bf:
    for pileupcolumn in bf.pileup(Chr, Pos-1, Pos+1):
        if pileupcolumn.pos == Pos:
            for read in [al for al in pileupcolumn.pileups if al.alignment.mapq>=MAPQ]:
                if not read.is_del and not read.is_refskip:
                    #print read.alignment.reference_name,read.alignment.pos + 1,read.alignment.query_sequence[read.query_position]
                    #print read.alignment.query_sequence[read.query_position]
                    Total += 1
                    base_count[read.alignment.query_sequence[read.query_position]] += 1

print "Chr\tPos\tCov\t" + "\t".join(Bases)
outlist = [Chr,Pos,Total]
for b in Bases:
    outlist.append(base_count[b])

print "\t".join(map(str,outlist))

#sf
