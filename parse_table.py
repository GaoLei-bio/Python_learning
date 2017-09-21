#!/usr/bin/env python

import sys

INPUT = sys.argv[1]

"""
command:
python XXXX.py INPUT > OUTPUT
"""

input_file = open(INPUT, 'U')

for line in input_file:
    line = line.strip()
    columns = line.split()

input_file.close()
