from flask import Flask


app = Flask(__name__)
app.config['DEBUG']=True

@app.route('/home', methods=['GET'])
def home():
    return 'Adeus'


app.run()