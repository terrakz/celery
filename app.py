import os
from flask import Flask
from tasks import count
import json
import time

app = Flask(__name__)

@app.route("/")
def get():
  result = count.delay()
  #while not result.ready():
    #time.sleep(2)
  return json.dumps(result.get())

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)
