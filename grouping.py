import csv,json,jieba

jieba.load_userdict("userdict.txt")

# adding = ["淺草", "葛西", "東京"]


target = json.load(open('target.json'))
output = {}

for item in target["table"]:
  cut_result = jieba.cut(item["title"], cut_all=False)
  # print(item["title"])
  # print(" : "+"/ ".join(cut_result))
  for each in cut_result:
    if each in output:
      output[each] += 1
    else:
      output[each] = 1

print(output)


# with open('cutfalse.json', 'w') as outfile:
    # json.dump(output, outfile)
