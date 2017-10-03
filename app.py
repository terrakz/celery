from flask import Flask
#from flask_restful import Resource, Api
from tasks import mytask
import subprocess
import requests
import httplib, urllib
import sys

app = Flask(__name__)
#api = Api(app)
#url = "http://130.239.81.63:5000"

@app.route('/', methods=['GET', 'POST'])
def get():
  #word = raw_input('Which pronoun: ')
  #mytask.delay(word)
  #word = requests.post(url, data = {'key':'value'})
  #print(word.text)
  #print('hello')
  #headers = {'token': 'mytoken'}
  #payload = "'key'='value'"
  #conn = httplib.HTTPSConnection('127.0.0.1:5000')
  #conn.request("POST", "", payload, headers)
  #response = conn.getresponse()
  #response_data = response.read()
  #conn.close()
  #return response_data
  #data = subprocess.check_output(["hello"])
  #return data
  word = sys.argv[0]
  return word
#api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
