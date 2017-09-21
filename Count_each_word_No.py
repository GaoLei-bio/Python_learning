# count numbers of each word
# Get word_list

import sys
import re
from operator import itemgetter
from collections import OrderedDict

INPUT = sys.argv[1]

word_regexp = re.compile('[a-zA-Z]+')

# Add word and its number to a dictionary
def add_words(word, words_dict):
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1

# process each line
def process_line(line, words_dict):
    line = line.strip()
    words_list = word_regexp.findall(line)
    for word in words_list:
        word = word.lower()
        add_words(word, words_dict)

# Sort by value and print
def print_result_v1(words_dict):
    val_key_list = []
    for key, val in words_dict.items():
        val_key_list.append((val, key))
    val_key_list.sort(reverse = True)
    print "%-10s%-10s" % ("word", "count")
    print "_" * 25
    for val, key in val_key_list:
        print "%-12s       %3d" % (key,val)

# Sort by value and print -- using OrderedDict
def print_result_v2(words_dict):
    sorted_dic = OrderedDict(sorted(words_dict.items(), key = itemgetter(1), reverse=True))
    #!!!!sorted_dis is a dictionary!!!!
    for k, v in sorted_dic.items():
        print "%-12s       %3d"  % (k, v)

# Sort by value then by key
def print_result_v3(words_dict):
    sorted_dic =  [v for v in sorted(words_dict.iteritems(), key=lambda(k, v): (-v, k))]
    #Unfortunately it will not work in the general case
    #(when - is not defined for the object or has different meaning)
    #but in this case the values are numbers, so it works
    #!!!!sorted_dis is a list!!!!
    for k, v in sorted_dic:
        print "%-12s       %3d"  % (k, v)


###################################
#Main program


words_dict = {}
input_file= open(INPUT, 'r')
for line in input_file:
    process_line(line, words_dict)
print "The length of the dictionary: ", len(words_dict)
print_result_v3(words_dict)
