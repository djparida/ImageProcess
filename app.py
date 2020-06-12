from flask import Flask, json, jsonify, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow # new
from flask_restful import Api, Resource # new
from flask_cors import CORS
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///image.db'

db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)
CORS(app, resources={r"/loan/*": {"origins": "*"}})

class ImageData(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    uname = db.Column(db.VARCHAR(20), nullable = True, unique=True)
    fname = db.Column(db.VARCHAR(20), nullable = True)
    lname = db.Column(db.VARCHAR(20), nullable = True)
    email = db.Column(db.VARCHAR(50), nullable = True, unique=True)
    image = db.Column(db.LargeBinary, nullable=True)

class ImageDataSchema(ma.Schema):
    class Meta:
        fields = ('id','uname','fname','lname','email','image')

image_schema = ImageDataSchema()
images_schema = ImageDataSchema(many=True)

