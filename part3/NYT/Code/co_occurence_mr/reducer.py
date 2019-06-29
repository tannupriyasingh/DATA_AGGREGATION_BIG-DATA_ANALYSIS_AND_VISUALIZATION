#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter

import sys

curr_word = ""
curr_count = 0
word = curr_word
wordpair = curr_word

for line in sys.stdin:
    line = line.strip()
    wordpair, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue
    if curr_word == wordpair:
        curr_count += count
    else:
        if curr_word:
            # write result to STDOUT
            print('%s\t%s' % (curr_word, curr_count))
        curr_count = count
        curr_word = wordpair

if curr_word == wordpair:
    print('%s\t%s' % (curr_word, curr_count))
