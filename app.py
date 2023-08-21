from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/initiatives")
def initiatives():
    return render_template('initiatives.html')