import os

for dirpath, dirnames, files in os.walk(os.path.abspath(os.curdir)+"/folder"):
  for name in files:
    #print name
    f = open("folder/"+name, 'r')
    #read = f.read()
    for line in f:
      #find beginning of text
      start = line.find("\"text\"") + 8
      print start

      #find ending of text
      end = line.find("\",", start)
      print end

      #count pronouns
      #count("bla") in line
      print line[start:end]
    #print read
