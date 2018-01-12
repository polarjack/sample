# encoding=utf-8
import json
import jieba
from pprint import pprint


items = json.load(open('target.json'))

output = {}

unique = 0

# print(content_result["日本"])

for (i, item) in enumerate(items["table"]):
  count = 0
  # print(item)
  cut_result = jieba.cut(item["title"], cut_all=False)
  for each in cut_result:
    if each in output:
        output[each] += 1
    else:
        output[each] = 1
        unique += 1

print(unique)

