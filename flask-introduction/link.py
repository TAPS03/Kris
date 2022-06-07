from flask import Flask, redirect, request, redirect 
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

app.config["SLQALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

db = SQLAlchemy(app)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    f_name = db.Column(db.String(30), nullable= False)
    l_name = db.Column(db.String(30), nullable= False)


db.create_all()

@app.route('/')
def hello_internet():
    return "<h1>egsgegseg<h1/>"

@app.route('/diff', methods= ["GET" , "POST"])
def hello_diff():
    if request.method == "POST":
        return "<h2>SIUUU<h2/>"
    else:
         return "<h2>SIUUU<h2/>"


@app.route('/hi')
def hi():
    return "<h5>you should leave<h5/>"

@app.route('/lol')
def lol ():
    return redirect ("http://www.Youtube.com")

if __name__ == '__main__' :
    app.run(debug=True, host = '0.0.0.0' , port =5000)

