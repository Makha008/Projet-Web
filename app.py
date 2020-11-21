from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
 return '<h1> Hello Dc </h1>'

@app.route('/ma_route/<name>')
def hello_name(name):
   return 'Hello %s!' % name

<<<<<<< HEAD

#######En utilisant les templates 
@app.route('/index/<name>')
def user(name):
    return render_template('index.html', name=name)

=======
@app.route('/index/')
def index():
    name = 'maharaja'
    return render_template('index.html', title='Hello', name=name)
>>>>>>> bcf75df1bdaf406970a666ff220cf5e4b92fad80

if __name__ == '__main__':
   app.run(debug = True)