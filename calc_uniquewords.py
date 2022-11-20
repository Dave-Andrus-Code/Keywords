# CALC_UNIQUEWORDS
# Written by DMA on 2022-11-18
# Unique words are valid English words, plus all the synonyms that mean the same thing.
# Unique words and their synonyms only appear once on this list.  If one word means two
# different things, the word with the most synonym wins.  If two words share a common number
# of synonyms, the alphabet wins.
#
# The first step of identifying unique words is caching all the words and their synonyms
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
# -----------------------------------------------------

import os, json, zlib, sys

# initialize dictionaries
wl_dict = {}    # the word list compiled from cached synonyms
wlsc_dict = {}  # word list synonym count

# Read the word list temp (WLT) files and build the dictionary.
for file in os.listdir():
    if file[:4] == 'wlt_':
        with open(file) as ofile:
            data = json.loads(ofile.read())
            wl_dict |= data

# Eliminate string sets for words without a synonym
for x in wl_dict:
    if not isinstance(wl_dict[x], list):
        if 'for the word:' in wl_dict[x]:
            wl_dict[x] = ['']
    else:
        wlsc_dict[x] = len(wl_dict[x])


# Sort the wordlist by the number of synonyms
wlsc_sorted = {key: val for key, val in sorted(wlsc_dict.items(), key=lambda ele: ele[1], reverse=True)}

# Remove inferior synonyms, keep only words with the greatest number of synonyms or none.
for x in wlsc_sorted.keys():
    if x in wl_dict:
        for y in wl_dict[x]:
            if x == y:
                # This shouldn't happen with clean data
                wl_dict[x].remove(y)
            else:
                # If a synonym of a higher-rated word exists in the dictionary,
                # remove the synonym
                if y in wl_dict:
                    del wl_dict[y]

with open("uniquewords_english.json", 'w') as outfile:
    outfile.write(json.dumps(wl_dict))

#print (wl_dict)
#print(wlsc_sorted)
#print (wlsc_dict)


