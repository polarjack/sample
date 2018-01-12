# encoding=utf-8
import json
import jieba
from pprint import pprint


items = json.load(open('target.json'))
# content_result = json.load(open('201706_content_count_jieba.json'))
# title_result = json.load(open('201706_attributes_count_jieba.json'))

filename = ["201706_content_count_jieba", "201707_content_count_jieba", "201708_content_count_jieba", "201706_attributes_count_jieba", "201707_attributes_count_jieba", "201708_attributes_count_jieba"]

output = {}

# print(content_result["日本"])
def render(name):
  input_data = json.load(open(name+".json"))
  for (i, item) in enumerate(items["table"]):
    count = 0
    # print(item)
    cut_result = jieba.cut(item["title"], cut_all=False)
    for each in cut_result:
      if each in input_data:
        # print(each)
        count += input_data[each]

    items["table"][i]["weight"] = count
    output[item["title"]] = count

# with open('contentver.json', 'w') as outfile:
#     json.dump(items, outfile)


# for (i, item) in enumerate(items["table"]):
#   count = 0
#   # print(item)
#   cut_result = jieba.cut(item["title"], cut_all=False)
#   for each in cut_result:
#     if each in title_result:
#       # print(each)
#       count += title_result[each]

#   items["table"][i]["weight"] = count
#   output[item["title"]] = count

render(filename[0])
render(filename[1])
render(filename[2])
render(filename[3])
render(filename[4])
render(filename[5])


with open('titlever.json', 'w') as outfile:
    json.dump(items, outfile)



# seg_list = jieba.cut(testing, cut_all=True)
# print("Full Mode: " + "/ ".join(seg_list))  # 全模式


# seg_list = jieba.cut(testing, cut_all=False)
# print("Full Mode: " + "/ ".join(seg_list))  # 全模式
