import os
from flask import Flask
from tasks import count
import json

app = Flask(__name__)

@app.route("/")
def get():
  result = count.delay()
  return json.dumps(result.get())

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)
