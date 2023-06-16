from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS
import requests
from flask_pymongo import PyMongo
app = Flask(__name__)
mongo_db = PyMongo(app, uri='mongodb://127.0.0.1:27017/crime_report')
db = mongo_db.db

#client = MongoClient('mongodb://localhost:27017/')  # Remplacez l'URL de connexion MongoDB appropriée
CORS(app)
# Route pour la page de connexion
@app.route('/login', methods=['POST'])
def login():
    username = request.json["username"]
    password = request.json["password"]
    print(username,password)
    user = db.users.find_one({'username': username})
    if user and user['password'] == password:
        # Authentification réussie
        response = {'message': 'Authentification réussie','code':200}
        return jsonify(response), 200
    else:
        # Authentification échouée
        response = {'message': 'Nom d\'utilisateur ou mot de passe incorrect','code':404}
        return jsonify(response), 404


# Route pour l'enregistrement du formulaire
@app.route('/register', methods=['POST'])
def enregistrer():
    username=request.json["username"]
    password=request.json["password"]
    password1=request.json["password1"]
    fullname=request.json["fullname"]
    mobile=request.json["mobile"]
    email=request.json["email"]
    adress=  request.json["adress"]

    # Création de l'objet à enregistrer dans la base de données
    formulaire = {
        'username': username,
        'email': email,
        'password':password,
        'password1': password1,
        'fullname':fullname,
        'mobile': mobile,
        'adress': adress
        }

    # Insertion du formulaire dans la collection
    db.users.insert_one(formulaire)

    # Réponse JSON pour indiquer que l'enregistrement a réussi
    response = {'message': 'Le formulaire a été enregistré avec succès','code':200}
    return jsonify(response), 200

if __name__ == '__main__':
    app.run()

