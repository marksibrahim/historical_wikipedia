import os
import json
from collections import defaultdict
import utilities

with open('../data/words_with_years.json') as f:
  words_with_years = json.load(f)

nums = dict()

years = range(1000, 2011, 10)

in_files = [f for f in os.listdir('../../metaphor/resources/thesaurus/word_lists/level_3_smushed/')]

for filename in in_files:
  with open('../../metaphor/resources/thesaurus/word_lists/level_3_smushed/' + filename, 'r') as ifile:
    category = ifile.readline().strip()
    words = []
    for line in ifile:
      if not line.strip() == '':
        word = line[:line.find('#')]
        #word_years = utilities.get_year(line[line.find('#')+1:line.rfind('#')])
        #words.append([word, word_years[0], word_years[1]])
        actual_word = utilities.get_actual_words([word])[0]
        if actual_word in words_with_years:
          words.append([word, words_with_years[actual_word]])

    words_at_year = dict()
    for year in years:
      words_at_year[year] = 0
      for word in words:
        if word[1] <= year:
          words_at_year[year] += 1
    print category
    nums[category] = words_at_year

print len(nums)

with open('../data/number_words_in_categories.json', 'w') as f:
  json.dump(nums, f)
