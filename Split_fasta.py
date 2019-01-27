#!/usr/bin/env python
# extract fasta sequence by their position
# Downloaded from http://www.bioinformatics-made-simple.com/2013/10/actually-i-have-hundreds-of-protein.html
import sys
import re


"""
python Split_fasta.py Input.fasta $prefix $piece_size
"""


FASTA= sys.argv[1]
prefix = sys.argv[2]
piece_size = int(sys.argv[3])

ID_list = []

fasta= open(FASTA, 'U')
fasta_dict= {}
for line in fasta:
    line= line.strip()                              # remove head and tail
    if line == '':                                  # if empty line, continue
        continue
    if line.startswith('>'):                        # If startswith ">", it's a seqname
        seqname= line.lstrip('>')                   # Get seqname
        #seqname= re.sub('\..*', '', seqname)        # Remove leftmost?
        fasta_dict[seqname]= ''                     # use the seqname as "key", assign a null value to it
        ID_list.append(seqname)
    else:
        fasta_dict[seqname] += line                 # use the following line(s) of seqs as "value"
fasta.close()

i = -1

for outname in ID_list:
    i += 1
    piece = '{0:06}'.format(i / piece_size)
    with open(prefix + piece + ".fa", 'a+') as small_file:
        small_file.write('>' + outname + "\n")
        small_file.write(fasta_dict[outname] + "\n")
