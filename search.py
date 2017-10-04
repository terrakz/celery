import os
import json

#count = 0
count = [0,0,0,0,0,0,0]
pronouns = ["han", "hon", "den", "det", "denne", "denna", "hen"]
#linenr = 1
path = "/mnt/volume/data/lab3/"
current = 1

for dirpath, dirnames, files in os.walk(os.path.abspath(os.curdir)+"/folder"):
#for dirpath, dirnames, files in os.walk(path):
  for name in files:
    f = open("folder/"+name, 'r')
    #f = open(path+name, 'r')

    for line in f:
      if not line.isspace() or not "\n":
        j = json.loads(line)
        print str(current) + " : " + j['text']
        text = j['text'].lower()
        for index,pronoun in enumerate(pronouns):
          count[index] += text.count(pronoun+" ") + text.count(" "+pronoun) + text.count(" "+pronoun+" ")
      current += 1

      #find beginning of text
      #start = line.find("\"text\"") + 8

      #find ending of text
      #end = line.find("\",", start)

      #count pronouns
      #print str(linenr) + ": " + str(line[start:end].lower().count("han"))
      #if "RT" not in line[start:start+2]:
       # count[0] += line[start:end].lower().count("han")
       # count[1] += line[start:end].lower().count("hon")
       # count[2] += line[start:end].lower().count("den")
       # count[3] += line[start:end].lower().count("det")
       # count[4] += line[start:end].lower().count("denna")
       # count[5] += line[start:end].lower().count("denne")
       # count[6] += line[start:end].lower().count("hen")
      #linenr += 1

#print count[0], count[1], count[2], count[3], count[4], count[5], count[6]
