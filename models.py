from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(200))

class Appareil(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marque = db.Column(db.String(50))
    modele = db.Column(db.String(50))
    date_sortie = db.Column(db.String(20))
    score = db.Column(db.Integer)
    categorie = db.Column(db.String(50))

class Telescope(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marque = db.Column(db.String(50))
    modele = db.Column(db.String(50))
    date_sortie = db.Column(db.String(20))
    score = db.Column(db.Integer)
    categorie = db.Column(db.String(50))