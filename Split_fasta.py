#!/usr/bin/env python
# split fasta file into small files

import sys
import re


"""
python 3
python Split_fasta.py Input.fasta $prefix $piece_size
"""


FASTA= sys.argv[1]
prefix = sys.argv[2]
piece_size = int(sys.argv[3])


i = -1

fasta= open(FASTA)
fasta_dict= {}
for line in fasta:
    #line= line.strip()                              # remove head and tail
    if line == '':                                  # if empty line, continue
        continue
    if line.startswith('>'):                        # If startswith ">", it's a seqname
        #seqname= line.lstrip('>')                   # Get seqname
        #seqname= re.sub('\..*', '', seqname)        # Remove leftmost?
        #fasta_dict[seqname]= ''                     # use the seqname as "key", assign a null value to it
        i += 1
        piece = '{0:06}'.format(i // piece_size)
        with open(prefix + piece + ".fa", 'a+') as small_file:
            small_file.write(line)
    else:
        #fasta_dict[seqname] += line                 # use the following line(s) of seqs as "value"
        with open(prefix + piece + ".fa", 'a+') as small_file:
            small_file.write(line)
fasta.close()
