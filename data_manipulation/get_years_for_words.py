import os
import json
import utilities

# Key: word
# Value: start date
words = dict()

# First we get all the words under level 1 categories
in_files = [f for f in os.listdir('../../metaphor/resources/thesaurus/word_lists/level_1_smushed/')]

# Loop through each file
for filename in in_files:
  with open('../../metaphor/resources/thesaurus/word_lists/level_1_smushed/' + filename, 'r') as ifile:
    # Ignore the category name
    print ifile.readline(),
    for line in ifile:
      if not line.strip() == '':
        word = line[:line.find('#')].lower()
        # Get rid of Old English parts of words that have transitioned
        if '<' in word:
          word = word[:word.find('<')].strip()
        
        # Sometimes a word has multiple spellings
        actual_words = utilities.get_actual_words([word])

        # Get the years for these words
        word_years = utilities.get_year(line[line.find('#')+1:line.rfind('#')])

        # Add each of the possible words
        for a_word in actual_words:
          # If we already have the word, and it's start date is earlier than this one, continue
          if a_word in words and words[a_word] < word_years[0]:
            continue
          else:
            # Otherwise store the word and start date
            words[a_word] = word_years[0]

print len(words)

with open('../data/words_with_years.json', 'w') as f:
  json.dump(words, f)


