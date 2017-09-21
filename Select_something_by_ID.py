#!/usr/bin/env python

import sys

INPUT = sys.argv[1]
SHARED_ID = sys.argv[2]

"""
command:
python Get_shared_blastout.on_contigs.py Old.blastout.on_contigs Shared.id > Shared.blastout.on_contigs
"""

input_file = open(INPUT, 'U')

Shared_id_set = set(open(SHARED_ID, 'U').read().split())



for line in input_file:
    if not line.startswith('#'):
        columns = line.strip().split()
        # Get >100 bp alignments on reference
        if columns[0] in Shared_id_set:
            print "\t".join(columns)

input_file.close()

#C0	$1 	query id
#C1	$2 	subject id
#C2	$3 	query length
#C3	$4 	subject length
#C4	$5 	alignment length
#C5	$6 	q. start
#C6	$7 	q. end
#C7	$8 	s. start
#C8	$9 	s. end
#C9	$10 	subject strand
#C10	$11 	% identity
#C11	$12 	identical
#C12	$13 	mismatches
#C13	$14 	gap opens
#C14	$15 	gaps
#C15	$16 	% query coverage per hsp
#C16	$17 	% query coverage per subject
#C17	$18 	score
#C18	$19 	bit score
#C19	$20 	evalue
