#!/usr/bin/env python
import sys


"""
command:

cat Input.fasta | python Simply_fasta_ID.py  Prefix  > Prefix.fasta
Output:
    Prefix.fasta
    Prefix.id_tab

"""
Prefix = sys.argv[1]

i = 0

with open(Prefix + ".id_tab", 'w') as tab_file:
    for line in sys.stdin:
        line = line.strip()
        if line.startswith(">"):
            i += 1
            new_id = Prefix + "_" + str(i)
            print ">" + new_id
            tab_file.write(new_id + "\t" + line[1:] + "\n")
        else:
            print line
