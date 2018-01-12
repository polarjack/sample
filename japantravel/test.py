import csv,json


target = json.load(open('aftersearch.json'))


for (i, item) in enumerate(target["articles"]):
  print(item["article_title"]) 