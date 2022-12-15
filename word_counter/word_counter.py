#!/usr/bin/env python3

"""Print list of words and the number of occurances in txt file

Prompt user for textfile and parse it to count the number of occurances of words
"""

# Prompt for filename
filename = input("File : ")

# open file
f = open(filename, "r")

#initialize empty dictionary
counts = dict()

# run over all lines in file
for line in f.readlines():
    words = line.split()
    # run over all words in line
    for word in words:
        # either create or increment counter for each word
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

print(counts)
