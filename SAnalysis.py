import json

total = 0
#open dictionary
json_data=open('dictionary.json')
jdata = json.load(json_data)
#open report and split into list of words
report = open("report.txt").read()
words = report.split()
#check the list of words against the dictionary and return value
for element in words:
  if element in jdata:
    value = jdata[element]
    total += value

print(total)

