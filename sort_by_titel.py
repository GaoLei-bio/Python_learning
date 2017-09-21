#!/usr/bin/env python
# extract fasta sequence by their position
# Downloaded from http://www.bioinformatics-made-simple.com/2013/10/actually-i-have-hundreds-of-protein.html
import sys
import re

RAW= sys.argv[1]
#SORTED= sys.argv[2]

fasta= open(RAW, 'U')
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

#out_file= open(SORTED, 'w')

for seqname in sorted(fasta_dict):
    print ">" + seqname + "\n" + fasta_dict[seqname]


#out_file.close()
sys.exit()
