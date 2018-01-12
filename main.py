# encoding=utf-8
import json
import jieba
from pprint import pprint


items = json.load(open('target.json'))
content_result = json.load(open('content_count_jieba.json'))
title_result = json.load(open('article_title_count_jieba.json'))

output = {}

# print(content_result["日本"])

for (i, item) in enumerate(items["table"]):
  count = 0
  # print(item)
  cut_result = jieba.cut(item["title"], cut_all=False)
  for each in cut_result:
    if each in content_result:
      # print(each)
      count += content_result[each]

  items["table"][i]["weight"] = count
  output[item["title"]] = count

with open('contentver.json', 'w') as outfile:
    json.dump(items, outfile)


for (i, item) in enumerate(items["table"]):
  count = 0
  # print(item)
  cut_result = jieba.cut(item["title"], cut_all=False)
  for each in cut_result:
    if each in title_result:
      # print(each)
      count += title_result[each]

  items["table"][i]["weight"] = count
  output[item["title"]] = count

with open('titlever.json', 'w') as outfile:
    json.dump(items, outfile)



# seg_list = jieba.cut(testing, cut_all=True)
# print("Full Mode: " + "/ ".join(seg_list))  # 全模式


# seg_list = jieba.cut(testing, cut_all=False)
# print("Full Mode: " + "/ ".join(seg_list))  # 全模式
