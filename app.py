## create a simple flask application
from flask import Flask,render_template

## create the flask app

app=Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/welcome')
def welcome():
    return "<h1>welcome to a new world</h1>"

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/success/<int:score>')
def success(score):
    return "You have passed the score is "+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "You have failed the score is "+str(score)

if __name__=='__main__' :
    app.run(debug = True)
