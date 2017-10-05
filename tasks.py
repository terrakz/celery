from celery import Celery
import os
import json

app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')


pronouns = {'han', 'hon', 'den', 'det', 'denna', 'denne', 'hen'}
path = "/mnt/volume/data/test/"

@app.task
def count():
  data = {'han':0,'hon':0,'den':0,'det':0,'denna':0,'denne':0,'hen':0}
  for dirpath, dirnames, files in os.walk(path):
    for name in files:
      f = open(path+name, 'r')

      for line in f:
        if not line.isspace(): #and len(line) > 1024: #last line in every file is 1024 in length but is not a json string
          j = json.loads(line)
          if not 'retweeted_status' in j:
            text = j['text'].lower().split(" ")
            for word in text:
              #word = word.strip(":")
              word = ''.join([i for i in word if i.isalpha()])
              if word in pronouns:
                data[word] += 1
  return data
