import os
import json

data = {'han':0,'hon':0,'den':0,'det':0,'denna':0,'denne':0,'hen':0}
#json_data = json.dumps(data)
pronouns = {'han', 'hon', 'den', 'det', 'denna', 'denne', 'hen'}
path = "/mnt/volume/data/"

#for dirpath, dirnames, files in os.walk(os.path.abspath(os.curdir)+"/folder"):
for dirpath, dirnames, files in os.walk(path):
  for name in files:
   # f = open("folder/"+name, 'r')
    f = open(path+name, 'r')

    for line in f:
      if not line.isspace() and len(line) > 1024: #last line in every file is 1024 in length but is not a json string
        j = json.loads(line)
        if j['retweeted'] == False: #doesnt seem to matter
          #print str(current) + " : " + j['text']
          text = j['text'].lower().split(" ")
          #print text
          #dict = json.loads(json_data)
          for word in text:
            if word in pronouns:
              data[word] += 1
            #data[pronoun] += text.count(pronoun+" ") + text.count(" "+pronoun) + text.count(" "+pronoun+" ")
          #for i in json_data:
            #print i[0]
          #for index,pronoun in enumerate(pronouns):
            #count[index] += text.count(pronoun+" ") + text.count(" "+pronoun) + text.count(" "+pronoun+" ")
            #data[pronoun] += text.count(pronoun+" ") + text.count(" "+pronoun) + text.count(" "+pronoun+" ")
            #print index, pronoun
      #current += 1
      #print count
    print data
    #dict = json.loads(json_data)
    #print json_data
    #for pronoun in pronouns:
      #print dict.get(pronoun)

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
