import json

with open('categories_decades_transformed.json', 'r') as f:
  categories = json.load(f)

years = range(1000, 2011, 50)

f = open('data.dsv', 'w')

cats = categories.keys()

f.write('date')
for category in cats:
  f.write('#' + category)
f.write('\n')

for year in years:
  f.write(str(year))
  for category in cats:
    if not str(year) in categories[category]:
      f.write('#0')
    else:
      f.write('#' + str(categories[category][str(year)]))
  f.write('\n')
