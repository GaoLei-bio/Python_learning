#!/usr/bin/env python

import sys
from operator import itemgetter
import re
import subprocess

Error = "usage: \n  python Py01_Parse_output.py  input.out > input.summary"

if len(sys.argv) < 2:
    sys.exit(Error)


TBL = sys.argv[1]
i = 0

masked_dict = {}
repClass_list = []

with open(TBL) as input_file:
    for line in input_file:
        i += 1
        if i > 3:
            cells = line.strip().split()
            repClass = cells[10]
            seq_id = cells[4]
            begin = int(cells[5])
            end = int(cells[6])
            if repClass not in masked_dict:
                repClass_list.append(repClass)
                masked_dict[repClass] = {}
                masked_dict[repClass][seq_id] = []
                masked_dict[repClass][seq_id].append([begin,end])
            else:
                if seq_id not in masked_dict[repClass]:
                    masked_dict[repClass][seq_id] = []
                    masked_dict[repClass][seq_id].append([begin,end])
                else:
                    masked_dict[repClass][seq_id].append([begin,end])

print "RepClass\tMasked_bp"
for repClass in repClass_list:
    masked_Num = 0
    for seq_id,hits_table in masked_dict[repClass].items():
        sorted_table = sorted(hits_table,key = itemgetter(0,1))
        start = sorted_table[0][0]
        end = sorted_table[0][1]
        merged_table = []
        for columns in sorted_table[1:]:
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
            masked_Num += columns[1] - columns[0] + 1
    print repClass + "\t" + str(masked_Num)













#srf
