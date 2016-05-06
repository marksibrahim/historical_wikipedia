import json

path = "~/Downloads/Entertainment.json"
with open(path, 'r') as f:
  a = json.load(f)

with open('../Entertainment.csv', 'w') as f:
  for x in a:
    f.write(str(x[0]) + ',' + str(x[1]) + '\n')
