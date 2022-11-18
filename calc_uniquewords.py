# CALC_UNIQUEWORDS
# Written by DMA on 2022-11-18
# Unique words are valid English words, plus all the synonyms that mean the same thing.
# Unique words and their synonyms only appear once on this list.  If one word means two
# different things, the word with the most synonym wins.  If two words share a common number
# of synonyms, the alphabet wins.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
# -----------------------------------------------------

from wordhoard import Synonyms
import json, time, os.path

# Get the file
try:
    wl = open('wordlist_english.txt', 'r', encoding='utf8')
except:
    print('ERROR:  Unable to open input file wordlist_english.txt.')
    raise SystemError

wordlist = wl.read().replace('\n', ' ').split(' ')

# Find all the synonyms and create a dictionary
word_dict = {}
synonyms_dict = {}
counter = 1
for word in wordlist:
    # firstword is used to determine if the chuck of 30-words has already been cached in a wlt file
    if counter == 1:
        firstword = word
    # The wordhoard rate limit kicks in at 30 words in 60 seconds.
    counter += 1

    # If the file has been parsed, skip the words in it.
    if os.path.exists('wlt_' + firstword):
        print('Skipping:  ' + word)
        if counter >= 30:
            counter = 1
    else:
        print('Getting:  ' + word)
        synonym = Synonyms(word)
        synonyms_results = synonym.find_synonyms()
        if synonyms_results is not None:
            synonyms_dict[word] = synonyms_results
        else:
            synonyms_dict[word] = 'no synonyms found'
        word_dict[word] = synonyms_dict[word]

        # Deal with the rate limit
        if counter >= 30:
            with open('wlt_' + firstword, 'w') as convert_file:
                convert_file.write(json.dumps(word_dict))
            word_dict = {}
            print ('\n...waiting on rate limit for ' + firstword + '...\n')
            counter = 1
            time.sleep(60)








