import csv,json,jieba

jieba.load_userdict("userdict.txt")

# adding = ["淺草", "葛西", "東京"]


target = json.load(open('cutfalse.json'))
japantravel = json.load(open('./../japantravel.json'))

# print(target)

print(len(japantravel["articles"]))

output = {"articles": []}

for (i, item) in enumerate(japantravel["articles"]):
  item["article_title"]
  cut_result = jieba.cut(item["article_title"], cut_all=False)
  print(item["article_id"])
  if not cut_result:
    continue
  elif cut_result is None:
    continue
  else:
    # print("inside: "+ item["article_id"])
    # print(" : "+"/ ".join(cut_result))
    for each in cut_result:
      if each == " ":
        print("empty")
      elif each in target:
        # print("Success: " + each)
        output["articles"].append(item)
        break
      else:
        print("")


# print(len(output))


with open('aftersearch.json', 'w') as outfile:
    json.dump(output, outfile)
