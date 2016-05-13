import json
import random

categories = ['The_Arts', 'Relative_position', 'Sport', 'Farming', 'Navigation', 'Direction', 'Legal_possession', 'Animals_collectively', 'Trading_organization', 'People_collectively']

for category in categories:
  with open('../viz_play/rankings/articles_for_tags/' + category + '.json', 'r') as f:
    a = json.load(f)

  with open('../data/csv/' + category + '.csv', 'w') as f:
    print category, len(a)
    sample = random.sample(xrange(len(a)), 100)
    for s in sample:
      x = a[s]
      f.write(str(x[0].encode('utf-8')) + '\t' + str(x[1]) + '\n')
