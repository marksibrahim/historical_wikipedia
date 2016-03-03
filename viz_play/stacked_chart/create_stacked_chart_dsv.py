import json

from operator import itemgetter

with open('../../data/categories_decades_transformed.json', 'r') as f:
  categories = json.load(f)

years = range(1000, 2011, 50)

f = open('categories.dsv', 'w')

cats = categories.keys()

order = sorted(zip(categories.keys(), [categories[category]['2000'] for category in categories.keys()]), key=itemgetter(1), reverse=True)

f.write('key#value#date\n')

for i in range(0, 10):
  category = order[i][0]
  for year in years:
    if not str(year) in categories[category]:
      val = '0'
    else:
      val =  str(categories[category][str(year)])
    f.write(category + '#' + val + '#' + str(year) + '\n')