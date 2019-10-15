#!/usr/bin/env python

import sys
from operator import itemgetter

'''
cat *.failed.gff3  | python merge_anno.py > Merged_gene_region.txt

'''

def add_to_dict(key, columns, dictionary):
    if key not in dictionary:
        dictionary[key] = []
        dictionary[key].append(columns)
    else:
        dictionary[key].append(columns)

def convert_int(fields):
    for i in range(0,len(fields)):
        if fields[i].isdigit() or (fields[i].startswith("-") and fields[i][1:].isdigit()):
            fields[i] = int(fields[i])
    return fields


anno_dict = {}

for line in sys.stdin:
    cells = convert_int(line.strip().split("\t"))
    contig = cells[0]
    Start = cells[3]
    End = cells[4]
    add_to_dict(contig, [min(Start,End),max(Start,End)], anno_dict)


for contig in sorted(anno_dict.keys()):
    chr_table = sorted(anno_dict[contig], key = itemgetter(0,1))
    start = chr_table[0][0]
    end = chr_table[0][1]
    merged_table = []
    for columns in chr_table[1:]:
        # if overlapping
        if columns[0] >= start and columns[0] <= end:
            start = min(start, columns[0])
            end = max(end, columns[1])
        else:
            merged_table.append([start, end])
            start = columns[0]
            end = columns[1]
    merged_table.append([start, end])
    for columns in merged_table:
        print contig + "\t" + "\t".join(map(str,columns))






#sf
