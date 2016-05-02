import json
import os

with open('../data/number_words_in_categories.json', 'r') as f:
  nums = json.load(f)

with open('../data/categories_decades_transformed.json', 'r') as f:
  tag_counts = json.load(f)

del tag_counts['None']

yes = 0
no = 0

for tag in tag_counts:
  num_tag = tag.replace('/', ' ')
  for year in tag_counts[tag]:
    if nums[num_tag][year] != 0:
      tag_counts[tag][year] = tag_counts[tag][year]/nums[num_tag][year]
      yes += 1
    else:
      no += 1
      # print tag, year
      # print nums[num_tag][year]
      # print tag_counts[tag][year]

print yes
print no

with open('../data/categories_decades_detrended_by_word_counts.json', 'w') as f:
  json.dump(tag_counts, f)

