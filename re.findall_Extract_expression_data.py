#!/usr/bin/env python

import sys
import re
"""

python Py01_Extract_expression_data.py $sam

"""

sample = sys.argv[1]

with open(sample + ".gtf") as input_file, open(sample + ".fpkm", "w") as fpkm_file, open(sample + ".tpm", "w") as tpm_file, open(sample + ".cov", "w") as cov_file:
    for line in input_file:
        if not line.startswith("#"):
            cells = line.strip().split("\t")
            if cells[2] == "transcript":
                exp_infor = cells[8]
                gene_id = re.findall(r'gene:(.*?)";',exp_infor)[0]
                cov = re.findall(r'cov "(.*?)";',exp_infor)[0]
                FPKM = re.findall(r'FPKM "(.*?)";',exp_infor)[0]
                TPM = re.findall(r'TPM "(.*?)";',exp_infor)[0]
                cov_file.write(gene_id + "\t" + cov + "\n")
                fpkm_file.write(gene_id + "\t" + FPKM + "\n")
                tpm_file.write(gene_id + "\t" + TPM + "\n")






















#sfs
