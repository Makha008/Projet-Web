from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
 return '<h1> Hello Dc </h1>'

@app.route('/ma_route/<name>')
def hello_name(name):
   return 'Hello %s!' % name

@app.route('/index/')
def index():
    name = 'maharaja'
    return render_template('index.html', title='Hello', name=name)

if __name__ == '__main__':
   app.run(debug = True)