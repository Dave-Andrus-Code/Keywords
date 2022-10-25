# KEYWORDS
# Written by DMA on 2022-10-23
# A simple string keyword extraction algorythm that summarizes the content.
# Originally intended to summarize job descriptions with similar job titles
# so I know what is most import aspects.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
# --------------------------------------------------------------------------------------------------------------------------------

# Imports
import os, argparse
import operator
import numpy as np
import scipy as stats
from collections import OrderedDict
from utils import *


# Globals
txtlines = {}   # All the text lines in a dictionary
keywords = {}   # All key works in a dictionary

# Prep
cmd = argparse.ArgumentParser(description='Parses keywords from a text file.')
cmd.add_argument('-f', dest='file', help='The path and filename to summarize.')
args = cmd.parse_args()

# Get the file
fname = args.file
if not fname:
    fname = os.path.join('.', 'sample', 'sample_remote_scrum_master.txt')
    print('No filename specified; using the sample file: ', fname)

try:
    f = open(fname, 'r', encoding='utf8')
except:
    print('ERROR:  Unable to open input file.')
    raise SystemError

# Read the file and 
for lines in f:
    line = strstrip(f.readline()).strip()
    
    # make a dictionary of unique lines
    if line not in txtlines:
        # lines with 3 words or less are typically headers in a hierachy and not useful here
        if line.strip().count(' ') > 3:
            txtlines[line] = []
    
    # make a dictionary of unique keywords
    for s in  line.split(' '):
        ls = s.lower()
        # check for plurals
        if ls[-1:] == 's' and ls not in snouns:
            ls = ls[0:len(ls)-1]
        # add the keyword if it's not ignored, blank, or only 1 character
        if ls not in ignore and ls != '' and len(ls) > 1:
            # Initialize the list if needed
            if ls not in keywords.keys():
                keywords[ls] = []
            if line not in keywords[ls]:
                # Add the line to the keyword
                keywords[ls].append(line)
                # Add the keyword to the line
                if line in txtlines:
                    txtlines[line].append(ls)

# Count the keywords
kcnt = {}
lsum = {}
for x in keywords:
    kcnt[x] = len(keywords[x])
for x in txtlines:
    lsum[x] = 0
    for y in txtlines[x]:
        lsum[x] = lsum[x] + kcnt[y]

# Sort the keyword dictionary by keyword count
sorted_tuples = sorted(kcnt.items(), key=operator.itemgetter(1), reverse=True)
sk = OrderedDict()
for k, v in sorted_tuples:
    sk[k] = v

# Sort the line dictionary by line score
sorted_tuples = sorted(lsum.items(), key=operator.itemgetter(1), reverse=True)
sl = OrderedDict()
for k, v in sorted_tuples:
    sl[k] = v

# Calculate the significance of keywords
arr = list(sk.values())
smean = np.mean(arr)
sserr = np.std(arr)
npsig = normal_dist(arr, smean, sserr)
sig = npsig.tolist()

# Calculate the significance of lines
larr = list(sl.values())
lsmean = np.mean(larr)
lsserr = np.std(larr)
lnpsig = normal_dist(larr, lsmean, lsserr)
lsig = lnpsig.tolist()

# Summary Output
c = 0
for x in sk:
    if sk[x] > 1 and 100-sig[c] > 94.99:
        # more than 1 keyword and keyword confidence > 95%
        l = 0   # line counter for lsig
        pk = 0  # t/f does this keyboard have at least 1 line with more than 80% confidence
        for z in sl:
            if z in keywords[x] and 100-lsig[l] > 79.99:
                pk = 1
            l = l + 1
        if pk == 1:
            print ('KEYWORD:  ', x, ' (' + str(round(100-sig[c], 2)) + '%)')
        
        l = 0   # line counter for lsig
        for z in sl:
            if z in keywords[x]:
                if 100-lsig[l] > 79.99:
                    # If confidence on the line is reasonably high, print it
                    # print ('  * (' + str(round(100-lsig[l], 2)) + '%)', z)
                    print ('  * (' + str(round(100-lsig[l], 2)) + '%)', excerpt(z.lower(), x, 3))
            l = l + 1
        print()
    c=c+1


