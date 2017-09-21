#!/usr/bin/env python
# extract fasta sequence by their position
# Downloaded from http://www.bioinformatics-made-simple.com/2013/10/actually-i-have-hundreds-of-protein.html
import sys
import re

"""
command:
python Extract_seq_by_ID.py INPUT.fa selected.id > selected.fasta
"""

FASTA= sys.argv[1]
ID= sys.argv[2]

fasta= open(FASTA, 'U')
fasta_dict= {}
for line in fasta:
    line= line.strip()                              # remove head and tail
    if line == '':                                  # if empty line, continue
        continue
    if line.startswith('>'):                        # If startswith ">", it's a seqname
        seqname= line.lstrip('>')                   # Get seqname
        seqname= re.sub('\..*', '', seqname)        # Remove leftmost?
        fasta_dict[seqname]= ''                     # use the seqname as "key", assign a null value to it
    else:
        fasta_dict[seqname] += line                 # use the following line(s) of seqs as "value"
fasta.close()

id= open(ID, 'U')
for line in id:
    outname= line.strip()
    #outname= line
    print('>' + outname)
    print(fasta_dict[outname])                 # seqname:line[0], from s to e. Important: s and e are "cardinal" numbers, not "ordinal" numbers
id.close()
sys.exit()
