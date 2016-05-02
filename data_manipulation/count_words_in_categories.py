import json
import os

nums = dict()

years = range(1000, 2011, 10)

in_files = [f for f in os.listdir('../../metaphor/resources/thesaurus/word_lists_2/3_smushed/')]

for filename in in_files:
  print filename[:-5].replace('_', ' ')
  with open('../../metaphor/resources/thesaurus/word_lists_2/3_smushed/' + filename) as f:
    words = json.load(f)
    words_at_year = dict()
    for year in years:
      words_at_year[year] = 0
      for word in words:
        if word[1] <= year and year <= word[2]:
          words_at_year[year] += 1
    nums[filename[:-5].replace('_', ' ')] = words_at_year

print len(nums)

with open('../data/number_words_in_categories.json', 'w') as f:
  json.dump(nums, f)