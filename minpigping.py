from unicodedata import name
from flask import Flask


app = Flask(__name__)

@app.route("/")
def Olá_Mundo():
    return"<h1>Olá Mundo</h1>"

@app.route("/ping")
def ping():
    return"<h1>você foi pingado</h1>"

@app.route("/<name>")
def diga_olá(name):
    return f"<h1>Olá sou {name}!</h1>"



app.run()