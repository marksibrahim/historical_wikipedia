import json
import operator

detrend = True

if detrend:
  with open('../data/categories_decades_detrended_by_word_counts.json', 'r') as f:
    categories = json.load(f)
else:
  with open('../data/categories_decades_transformed.json', 'r') as f:
    categories = json.load(f)

# for category in categories:
#   for key in categories[category]:
#     if categories[category][key] == None:
#       categories[category][key] = 0

years = range(1000, 2001, 20)

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
  with open('../viz_play/rankings/grid_detrended.json', 'w') as o:
    json.dump(grid, o)
else:
  with open('../viz_play/rankings/grid.json', 'w') as o:
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
  with open('../viz_play/rankings/graph_detrended.json', 'w') as f:
    json.dump(graph, f)
else:
  with open('../viz_play/rankings/graph.json', 'w') as f:
    json.dump(graph, f)
