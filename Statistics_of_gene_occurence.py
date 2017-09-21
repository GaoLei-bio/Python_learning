#!/usr/bin/env python

import sys
import  numpy
INPUT = sys.argv[1]


"""
command:
python Statistics_of_gene_occurence.py Input.gff3 >> Gene_occurence.txt
"""

input_file = open(INPUT, 'U')

print "INPUT\tSeq_having_Gene\tGene_number\tstart_codon\tstop_codon\tComplete_gene\tTotal_gene_length\tTotal_length_std\tComplete_gene_length"

Seq_having_Gene_number = 0
Gene_number = 0
start_codon_No = 0
stop_codon_No = 0
Complete_gene_number = 0
Gene_length = 0
Complete_gene_length = 0

Seq_having_Gene_list = []
gene_have_start_list = []
gene_have_stop_list = []
gene_len_dict = {}


for line in input_file:
    columns = line.strip().split()
    if columns[2] == "gene":
        Gene_number += 1
        gene_id = columns[8].replace("ID=", "")
        gene_len = int(columns[4]) - int(columns[3]) + 1
        Gene_length = Gene_length + gene_len
        Seq_having_Gene_list.append(columns[0])
        gene_len_dict[gene_id] = gene_len

    if columns[2] == "start_codon":
        start_codon_No += 1
        gene_id = columns[8].replace("Parent=", "").split(".")[0]
        gene_have_start_list.append(gene_id)
    if columns[2] == "stop_codon":
        stop_codon_No += 1
        gene_id = columns[8].replace("Parent=", "").split(".")[0]
        gene_have_stop_list.append(gene_id)

# Count the seqs having gene
Seq_having_Gene_set = set(Seq_having_Gene_list)
Seq_having_Gene_number = len(Seq_having_Gene_set)

# Count complete gene
gene_have_start_set = set(gene_have_start_list)
gene_have_stop_set = set(gene_have_stop_list)
Complete_gene_set = gene_have_start_set.intersection(gene_have_stop_set)
Complete_gene_number = len(Complete_gene_set)

# Get total length of complete gene
Complete_gene_list = list(Complete_gene_set)
for gene_id in Complete_gene_list:
    Complete_gene_length = Complete_gene_length + gene_len_dict[gene_id]

# calculate standard deviation using numpy.std()
len_std = numpy.std(gene_len_dict.values())



print INPUT.replace(".gff3", "") + "\t" + str(Seq_having_Gene_number) + "\t" + str(Gene_number) + "\t" + str(start_codon_No) + "\t" + str(stop_codon_No) + "\t" + str(Complete_gene_number) + "\t" + str(Gene_length) + "\t" + str(len_std) + "\t" + str(Complete_gene_length)


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
