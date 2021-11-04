from flask import Flask
from flask_cors import CORS
from .constants import SQLALCHEMY_DATABASE_URI


app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = 0
