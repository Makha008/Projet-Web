from flask import Flask
from flask import render_template
from flask import jsonify
from flask import  request,json


app = Flask(__name__)

book=[
    {
        'id':1,
        'titre' : 'un titre',
    },
    {
        'id':2,
        'titre': 'un autre titre random',
    },
]



@app.route("/")
def home():
 return '<h1> My app </h1>'

@app.route('/api/books/', methods=['GET'])
def api():
    return jsonify(book)
  
@app.route('/api/books/<int:id_book>', methods=['GET'])

def Rechercher_par_id(id_book): 
    liste_id = []
    for k in book:
        if k['id'] == id_book:
            liste_id.append(k)
            return jsonify(liste_id)
        else :
            return 'Aucun book ne porte cet id'

@app.route('/api/books/<string:t_book>',methods=['GET'])
def Rechercher_par_titre(t_book): 
    liste_titre=[]
    for k in book:
        if k['titre']==t_book:
            liste_titre.append(k)
            return jsonify(liste_titre)
        else:
            return 'aucun book ne porte ce titre'
                
        



if __name__ == '__main__':
   app.run(debug = True)