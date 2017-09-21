#!/usr/bin/env python
# Shuffle seqs
# 
import sys
import numpy as np

"""
command:
python Shuffle_seq.py INPUT.fa > shuffle.fasta
"""

FASTA= sys.argv[1]


fasta= open(FASTA, 'U')
fasta_dict= {}
title_list = []

for line in fasta:
    line= line.strip()                              # remove head and tail
    if line == '':                                  # if empty line, continue
        continue
    if line.startswith('>'):                        # If startswith ">", it's a seqname
        seqname= line.lstrip('>')                   # Get seqname
        title_list.append(seqname)
        fasta_dict[seqname]= ''                     # use the seqname as "key", assign a null value to it
    else:
        fasta_dict[seqname] += line                 # use the following line(s) of seqs as "value"
fasta.close()

# using np.random.shuffle
np.random.shuffle(title_list)

for outname in title_list:
    print('>' + outname)
    print(fasta_dict[outname])                 # seqname:line[0], from s to e. Important: s and e are "cardinal" numbers, not "ordinal" numbers

sys.exit()
