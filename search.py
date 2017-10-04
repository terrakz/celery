import os

count = 0
#linenr = 1
path = "/mnt/volume/data/lab3/"

#for dirpath, dirnames, files in os.walk(os.path.abspath(os.curdir)+"/folder"):
for dirpath, dirnames, files in os.walk(path):
  for name in files:
    #f = open("folder/"+name, 'r')
    f = open(path+name, 'r')

    for line in f:
      #find beginning of text
      start = line.find("\"text\"") + 8

      #find ending of text
      end = line.find("\",", start)

      #count pronouns
      #print str(linenr) + ": " + str(line[start:end].lower().count("han"))
      count += line[start:end].lower().count("han")
      #linenr += 1

print count
