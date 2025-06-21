from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello,World!"

@app.route("/data")
def numbers():
    return "12345678"

@app.route("/<name>")
def return_name(name):
    return "Hello, your name is {name}"

app.run(port=5001)