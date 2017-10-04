import os

count = 0

for dirpath, dirnames, files in os.walk(os.path.abspath(os.curdir)+"/folder"):
  for name in files:
    f = open("folder/"+name, 'r')

    for line in f:
      #find beginning of text
      start = line.find("\"text\"") + 8

      #find ending of text
      end = line.find("\",", start)

      #count pronouns
      print line[start:end].count("han")
      count += line[start:end].count("han")

print count
