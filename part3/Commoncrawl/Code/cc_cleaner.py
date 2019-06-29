#!/usr/bin/python3

import glob
import json
import re
import os

# We are reading the entire commoncrawl data and loading it here.
files_list = glob.glob(os.path.join(os.getcwd(), "../commoncrawl_raw_data/*.txt"))

cc_corpus = []

# For each of our raw file, we remove URLs and few of the very common not required characters and escape characters.
for file in files_list:
    print(file)
    data = open(file, "r")
    data = data.read()
    data = data.encode().decode("utf-8")
    data = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', data, flags=re.MULTILINE)
    data = re.sub(r'([@#]+)', '', data, flags=re.MULTILINE)
    data = data.replace("&amp;", "")
    data = data.replace("&lt;", "")
    cc_corpus.append(data)

# Once all that is done we save it to one big file that can be used for overall
# Pre-processing and then split into multiple files for Word Count and Co-occurence.
cc_final_text = '\n'.join(cc_corpus)
cc_file = open("ccData1.txt", "w")
cc_file.write(cc_final_text)
cc_file.close()


