
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/hello")
def hello():
    return jsonify({
        "message": "Hello from Python running on Azure!"
    })
