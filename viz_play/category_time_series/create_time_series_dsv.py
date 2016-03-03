import json

with open('../../data/categories_decades_detrended.json', 'r') as f:
 categories = json.load(f)
# with open('../../data/categories_decades.json', 'r') as f:
#   categories = json.load(f)

years = range(1000, 2011, 50)

# f = open('data.dsv', 'w')
f = open('data_detrended.dsv', 'w')

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

f.close()
