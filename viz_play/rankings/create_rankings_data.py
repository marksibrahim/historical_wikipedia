import json
import operator

detrend = True

if detrend:
  with open('../../data/categories_decades_detrended.json', 'r') as f:
    categories = json.load(f)
else:
  with open('../../data/categories_decades_transformed.json', 'r') as f:
    categories = json.load(f)

years = range(1000, 2001, 100)

cats = categories.keys()

grid = []
ranks = dict()
graph = []

for year in years:
  # Sorted tuples are ('category id', degree at current year)
  tuples_to_be_sorted = [(category, categories[category][str(year)] if str(year) in categories[category] else 0) for category in cats]
  sorted_tuples = sorted(tuples_to_be_sorted, key=operator.itemgetter(1), reverse=True)

  ranks[year] = dict()
  for z in range(0, len(sorted_tuples)):
    ranks[year][sorted_tuples[z][0]] = z

  for y in range(0, len(sorted_tuples)):
    t = sorted_tuples[y]
    if year == 1000:
      grid.append({'id': str(y)})
    grid[y][str(year)] = t[0] + ' (' + str(int(t[1])) + ')'

if detrend:
  with open('grid_detrended.json', 'w') as o:
    json.dump(grid, o)
else:
  with open('grid.json', 'w') as o:
    json.dump(grid, o)

for category in cats:
  values = []
  catranks = []
  for year in years:
    rank = ranks[year][category]
    catranks.append({'date': year, 'value': rank})
    if not str(year) in categories[category]:
      values.append({'date': year, 'value': 0})
    else:
      values.append({'date': year, 'value': categories[category][str(year)]})
  graph.append({'name': category, 'values': values, 'ranks': catranks})

if detrend:
  with open('graph_detrended.json', 'w') as f:
    json.dump(graph, f)
else:
  with open('graph.json', 'w') as f:
    json.dump(graph, f)
