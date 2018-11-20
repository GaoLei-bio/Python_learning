#!/usr/bin/env python

import sys
from operator import itemgetter

Error = "usage: \n  python Py02_bin_map_for_Rqtl.py 03_bin_out.$chrId.csv chrPre RIL_list.$chrId Bin_pos.$chrId >> 04_bin_map_for_Rqtl.csv \n    chrPre is prefix of chromosome id. e.g. SL3.0ch for SL3.0ch01"

if len(sys.argv) < 2:
    sys.exit(Error)


INPUT = sys.argv[1]
chrPre = sys.argv[2]
RIL_list_file = sys.argv[3]
Bin_pos_file = sys.argv[4]

''' Step 1 read bin output from snpbinner  bins '''
RIL_list = []
RIL_gt_dict = {}

with open(INPUT) as input_file:
    for line in input_file:
        columns = line.strip().split(",")
        if line.startswith("##binmap id"):
            binmap_id_line = columns
        elif line.startswith("##bin start"):
            bin_start_line = columns
        elif line.startswith("##bin end"):
            bin_end_line = columns
        elif line.startswith("bin center"):
            bin_center_line = columns
        else:
            # ril gt line
            RIL_name = columns[0]
            RIL_id = int(RIL_name.replace("RIL_",""))
            RIL_list.append([RIL_name,RIL_id])
            RIL_gt_dict[RIL_name] = columns

''' Step 2 Output bin map '''

sorted_RIL_list = sorted(RIL_list, key = itemgetter(1))

with open(RIL_list_file,'w') as RIL_check_file, open(Bin_pos_file,'w') as bin_check_file:
    RIL_check_file.write("RIL_name\tRIL_id\n")
    for ril in sorted_RIL_list:
        ril[1] = str(ril[1])
        RIL_check_file.write("\t".join(ril) + "\n")

    bin_check_file.write("BinMarker\tChrName\tChrId\tStart\tEnd\tCenter\n")

    chr_name = binmap_id_line[1]
    chr_id = str(int(chr_name.replace(chrPre,"")))
    columns_number = len(binmap_id_line)
    for i in range(1,columns_number):
        BinMarker = "Marker_" + chr_id + "_" + str(i)
        Bin_pos_line = [BinMarker,chr_name,chr_id,bin_start_line[i],bin_end_line[i],bin_center_line[i]]
        bin_check_file.write("\t".join(Bin_pos_line) + "\n")

        bin_map_out_list = [BinMarker,chr_id]
        for ril in sorted_RIL_list:
            RIL_name = ril[0]
            if RIL_gt_dict[RIL_name][i] == "a":
                bin_map_out_list.append("A")
            elif RIL_gt_dict[RIL_name][i] == "b":
                bin_map_out_list.append("H")
            else:
                bin_map_out_list.append("NA")
        print ",".join(bin_map_out_list)






#srf
