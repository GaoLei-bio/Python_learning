"""
usage: Py01_Vcf_to_CrosspointsIn.py [-h] [--snpMissCutoff SNPMISSCUTOFF]
                                    [--excludeChr EXCLUDECHR]
                                    vcf_file

positional arguments:
  vcf_file              Path to snnpbinnner bins output

optional arguments:
  -h, --help            show this help message and exit
  --snpMissCutoff SNPMISSCUTOFF
                        Float, maximal missing ratio of SNPs in RILs
  --excludeChr EXCLUDECHR
                        The chromosome(s) you want to exclude from the QTL
                        analysis (e.g. chr00,chr01)

"""
import argparse
from pathlib import Path
from operator import itemgetter

parser = argparse.ArgumentParser()
parser.add_argument("vcf_file", type=Path, help="Path to snnpbinnner bins output")
parser.add_argument("--snpMissCutoff", type=str, help="Float, maximal missing ratio of SNPs in RILs", required=False, default="")
parser.add_argument("--excludeChr", type=str, help="The chromosome(s) you want to exclude from the QTL analysis (e.g. chr00,chr01)", required=False, default="")

args = parser.parse_args()
# Namespace(excludeChr='chr00', snpMissCutoff='0.5', vcf_file=PosixPath('SNP.vcf'))

excludeChr = set(args.excludeChr.split(","))

if len(args.snpMissCutoff) > 0:
    snpMissCutoff = float(args.snpMissCutoff)
else:
    snpMissCutoff = 1.0



def recode(out_line,columns,a,b,h,m):
    for cell in columns[5:]:
        if cell == a:
            out_line.append("a")
        elif cell == b:
            out_line.append("b")
        elif cell == h:
            out_line.append("h")
        elif cell == m:
            out_line.append("-")



''' Step 01 parse vcf file'''
chr_list = []
SNP_raw_GT = "00_SNP_raw_GT.txt"

with args.vcf_file.open() as input_file, open(SNP_raw_GT,"w") as output_gt, open("chromosome.info",'w') as chr_inf:
    for line in input_file:
        if line.startswith("##contig=<ID="):
             # chromosome infor line
             raw_chr_id = line.strip().replace("##contig=<ID=","").split(",")[0]
             chr_len = line.strip().replace("##contig=<ID=","").split(",")[1].split("=")[1].split(">")[0]
             if raw_chr_id not in excludeChr:
                 chr_inf.write(raw_chr_id + "|" + chr_len + "\n")
                 chr_list.append(raw_chr_id)
        elif not line.startswith("##"):
            columns = line.strip().split()
            if columns[0] not in excludeChr:
                if line.startswith("#CHROM"):
                    # This is table head
                    outline = ["Missing","Chrom",	"Position"] + columns[9:]
                    total_RIL = float(len(columns[9:]) - 2)
                    output_gt.write("\t".join(outline) + "\n")
                    #print ("\t".join(outline))
                    with open("Error_SNP", "w") as small_file:
                        small_file.write("\t".join(outline) + "\n")
                    with open("Error_vcf", "w") as small_file:
                        small_file.write(line)
                    with open("Revised_SNP", "w") as small_file:
                        small_file.write("\t".join(outline) + "\n")
                    with open("Revised_vcf", "w") as small_file:
                        small_file.write(line)
                else:
                    outline = []
                    outline.append(columns[0])
                    #outline.append(columns[0])
                    outline.append(columns[1])
                    miss_number = 0
                    for gt in columns[9:]:
                        # 0/0  =  0
                        # 0/1  =  1
                        # 1/1  =  2
                        # ./.  =  ?
                        if gt.startswith("0/0"):
                            outline.append("0")
                        elif gt.startswith("0/1"):
                            outline.append("1")
                        elif gt.startswith("1/1"):
                            outline.append("2")
                        else:
                            outline.append("?")
                            miss_number += 1
                    missed = str(miss_number/total_RIL)
                    if (outline[2] == "0" and outline[3] == "2") or (outline[2] == "2" and outline[3] == "0"):
                        # parents are homo
                        output_gt.write(missed + "\t" + "\t".join(outline) + "\n")
                        # print (missed + "\t" + "\t".join(outline))
                    else:
                        if outline[4:].count("0")/total_RIL < 0.1 or outline[4:].count("2") /total_RIL < 0.1:
                            # >= 1 parent is hetero; most of RILs have only one GT
                            with open("Error_SNP", "a+") as small_file:
                                small_file.write("\t".join(outline) + "\n")
                            with open("Error_vcf", "a+") as small_file:
                                small_file.write(line)
                        else:
                            # >= 1 parent is hetero; RILs have both GTs
                            with open("Revised_SNP", "a+") as small_file:
                                small_file.write("\t".join(outline) + "\n")
                            with open("Revised_vcf", "a+") as small_file:
                                small_file.write(line)
                            if outline[2] == "0":
                                outline[3] = "2"
                            elif outline[2] == "2":
                                outline[3] = "0"
                            elif outline[3] == "0":
                                outline[2] = "2"
                            elif outline[3] == "2":
                                outline[2] = "0"

                            #print (missed + "\t" + "\t".join(outline))
                            output_gt.write(missed + "\t" + "\t".join(outline) + "\n")



''' Step 02
    parse SNP_raw_GT
    output crosspoints_in.tsv
'''

i = -1
marker_gt_dict = {}

with open(SNP_raw_GT) as raw_gt, open("01_Excluded_marker.txt", 'w') as excluded_marker:
    for line in raw_gt:
        i += 1
        columns = line.strip().split("\t")
        if i == 0:
            # head line
            head_line = ["marker","position(bp)"] + columns[5:]
            excluded_marker.write(line)
        else:
            missing = float(columns[0])
            if missing > snpMissCutoff:
                excluded_marker.write(line)
            else:
                raw_chr_id = columns[1]
                columns[2] = int(columns[2])
                if raw_chr_id not in marker_gt_dict:
                    marker_gt_dict[raw_chr_id] = []
                    marker_gt_dict[raw_chr_id].append(columns)
                else:
                    marker_gt_dict[raw_chr_id].append(columns)

for raw_chr_id in chr_list:
    with open("01_crosspoints_in." + raw_chr_id + ".tsv", "w") as crosspoints_in:
        crosspoints_in.write("\t".join(head_line) + "\n")
        # sort
        sorted_table = sorted(marker_gt_dict[raw_chr_id], key = itemgetter(2))
        for columns in sorted_table:
            columns[2] = str(columns[2])
            marker = columns[1] + "_" + columns[2]
            pos = columns[2]
            out_line = [marker,pos]
            if columns[3] == "2":
                # LA2093 == "2"
                a = '0'
                b = '2'
                h = '1'
                m = '?'
                recode(out_line,columns,a,b,h,m)

            elif columns[3] == "0":
                # LA2093 == "0"
                a = '2'
                b = '0'
                h = '1'
                m = '?'
                recode(out_line,columns,a,b,h,m)
            crosspoints_in.write("\t".join(out_line) + "\n")













#srf
