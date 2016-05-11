import json

with open('../data/categories_sample_articles.json', 'r') as f:
  articles = json.load(f)['list_of_article_year_tuples']

for category in articles:
  new_name = category.replace('/', '_')
  new_name = new_name.replace(' ', '_')
  with open('../viz_play/rankings/articles_for_tags/' + new_name + '.json', 'w') as f:
    json.dump(articles[category], f)

with open('../viz_play/rankings/tags.json', 'w') as f:
  json.dump(articles.keys(), f)