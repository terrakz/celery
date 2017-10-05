import os
import json

data = {'han':0,'hon':0,'den':0,'det':0,'denna':0,'denne':0,'hen':0}
#json_data = json.dumps(data)
pronouns = {'han', 'hon', 'den', 'det', 'denna', 'denne', 'hen'}
path = "/mnt/volume/data/"

for dirpath, dirnames, files in os.walk(os.path.abspath(os.curdir)+"/folder"):
#for dirpath, dirnames, files in os.walk(path):
  for name in files:
    f = open("folder/"+name, 'r')
    #f = open(path+name, 'r')

    for line in f:
      if not line.isspace() and len(line) > 1024: #last line in every file is 1024 in length but is not a json string
        j = json.loads(line)
        if j['retweeted'] == False: #doesnt seem to matter
          #print str(current) + " : " + j['text']
          text = j['text'].lower().split(" ")
          #dict = json.loads(json_data)
          for word in text:
            word = word.strip(":")
            if word in pronouns:
              data[word] += 1
    print data
    #dict = json.loads(json_data)
