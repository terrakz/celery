import os
from flask import Flask, render_template, request
from tasks import count

app = Flask(__name__)

@app.route("/")
def get():
  result = count.delay()
  result.wait()
  return result

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)
