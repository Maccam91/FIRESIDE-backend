import os
import pymongo
from flask import Flask, request, render_template
from dotenv import load_dotenv
from flask_cors import CORS
from user.models import User


load_dotenv()
URI = os.getenv("MONGO_URI")

app = Flask(__name__, static_folder='E:/sei1213/unit4/CAPSTONE/CAPSTONE/frontend', static_url_path='')
# app.secret_key = b'\xc3"$T\xb8\xf7\xe5J\x8b0\xad\x08\xee\x9a]\x91'
client = pymongo.MongoClient(URI)
db = client.fire_side


@app.route('/')
def homePage():
    return render_template('home.html')

@app.route('/user/signup', methods=['POST'])
def signup():
 return User().signup()
# @app.route('/user', method=['GET'])




# @app.route('/classes')
# def classPage():
#     return {"Class":["This is the classes page"]}


# @app.route('/classes/create')
# def createClass():
#     return '<h1>Create a Class Here</h1>'


# @app.route('/monsters')
# def monsterPage():
#     return {"Monster": ["this is the monster page"]}


# @app.route('/monsters/create', methods=['POST', 'GET'])
# def createMonster():
#     print(request.get_json())
#     return "<h1>Create a Monster Here</h1>"


# @app.route('/items')
# def itemList():
#     return {"Item List Page":["Item 1","Item 2", "Item 3"]}
# @app.route('/spells')
# def spellTable():
#     return {"Spells":["spell 1 ", "spell 2"]}
# @app.route('/abilities')
# def abilityTable():
#     return {"Abilites":["Abilites will go here"]}


if __name__ == "__main__":
    app.run(debug=True)
