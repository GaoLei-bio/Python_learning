#!/usr/bin/env python
# Shuffle seqs
#
import sys
import numpy as np

"""
command:
python Shuffle_list.py INPUT.list > shuffled.list
"""

RAW_LIST = sys.argv[1]

raw_list = open(RAW_LIST, 'U').read().split()

np.random.shuffle(raw_list)
print("\n".join(raw_list))        

sys.exit()
