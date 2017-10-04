import os

for dirpath, dirnames, files in os.walk(os.path.abspath(os.curdir)+"/folder"):
  for name in files:
    print name
    f = open("folder/"+name, 'r')
    read = f.read()
    print read
