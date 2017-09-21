#!/usr/bin/env python

import sys

INPUT = sys.argv[1]
OUTPUT = sys.argv[2]
"""
command:
python Get_wanted_coords.py INPUT  OUTPUT
"""

input_file = open(INPUT, 'U')
output_file = open(OUTPUT, 'w')

for line in input_file:
    line = line.strip().replace(":", "__")
    columns = line.split()
    if columns[11] != columns[12]:
        if float(columns[7]) >= float(columns[8]):
            output_file.write("\t".join(columns[0:13]) + "\n")

input_file.close()
output_file.close()

# c0 $1	[S1]
# c1 $2	[E1]
# c2 $3	[S2]
# c3 $4	[E2]
# c4 $5	[LEN 1] Alignment_length
# c4 $6	[LEN 2] Alignment_length
# c6 $7	[% IDY] Indentity
# c7 $8	[LEN R] Reference_chr length
# c8 $9	[LEN Q] Query Contigs
# c9 $10	[COV R] Percentage of covered base of Reference_chr
# c10 $11	[COV Q] Percentage of covered base of Query contigs
# c11 $12	[TAGS]
# c12 $13	Contig_ID
# c13 $14	Annotation
