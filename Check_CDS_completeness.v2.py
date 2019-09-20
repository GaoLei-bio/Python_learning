#!/usr/bin/env python
# extract fasta sequence by their position
# Downloaded from http://www.bioinformatics-made-simple.com/2013/10/actually-i-have-hundreds-of-protein.html
import sys
import re

import argparse
from pathlib import Path
from operator import itemgetter

parser = argparse.ArgumentParser()
parser.add_argument("--FASTA", type=str, help="Input fasta seq file", required=True, default="")
parser.add_argument("--SeqType", type=str, help="Sequence type: protein or CDS", required=True, default="")

args = parser.parse_args()

FASTA = args.FASTA
SeqType = args.SeqType

""" Function """
def cds_check(Seq):
    good_stops = set(["TAG","TGA","TAA"])

    Start_codon = Seq[0:3]
    Stop_codon = Seq[-3:]
    if len(Seq) % 3 != 0:
        Conclusion = "Frameshift"
    else:
        if Start_codon == "ATG" and Stop_codon in good_stops:
            Conclusion = "Complete"
        elif Start_codon == "ATG":
            Conclusion = "Bad_Stop"
        elif Stop_codon in good_stops:
            Conclusion = "Bad_Start"
        else:
            Conclusion = "Bad_Both"
    i = 3
    Premature_stop_codon = 0
    while i < len(Seq)-3:
        if Seq[i:i+3] in good_stops:
            Premature_stop_codon += 1
        i = i + 3
    if Premature_stop_codon > 0:
        Conclusion = Conclusion + "|Premature_stop_codon"
    outlist = [Start_codon,Stop_codon,str(Premature_stop_codon),Conclusion]
    return outlist


""" Check CDS """
if SeqType == "CDS":
    head_list = ['Seq','Start_codon','Stop_codon',"Premature_stop_codon",'Conclusion']
    print "\t".join(head_list)


fasta= open(FASTA, 'U')
seq = ''
for line in fasta:
    line= line.strip()                              # remove head and tail
    if line == '':                                  # if empty line, continue
        continue
    if line.startswith('>') and seq == '':                        # If startswith ">", it's a seqname
        seqname= line.lstrip('>')                   # Get seqname
        #seqname= re.sub('\..*', '', seqname)        # Remove leftmost?
    elif line.startswith('>') and seq != '':
        if SeqType == "CDS":
            outlist = cds_check(seq)
        print seqname + "\t" + "\t".join(outlist)
        seqname = line.lstrip('>')
        seq = ''
    else:
        seq += line                 # use the following line(s) of seqs as "value"
fasta.close()


if SeqType == "CDS":
    outlist = cds_check(seq)
print seqname + "\t" + "\t".join(outlist)




#sf
