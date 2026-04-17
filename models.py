from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Modèles de données pour les utilisateurs, les appareils, les télescopes et les photos
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(200))
    photos = db.relationship('Photo', backref='user', lazy=True, cascade='all, delete-orphan')

    # Représentation de l'utilisateur pour le débogage
class Appareil(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marque = db.Column(db.String(50))
    modele = db.Column(db.String(50))
    date_sortie = db.Column(db.String(20))
    score = db.Column(db.Integer)
    categorie = db.Column(db.String(50))

    # Représentation de l'appareil pour le débogage
class Telescope(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marque = db.Column(db.String(50))
    modele = db.Column(db.String(50))
    date_sortie = db.Column(db.String(20))
    score = db.Column(db.Integer)
    categorie = db.Column(db.String(50))

    # Représentation du télescope pour le débogage
class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(120), nullable=False)
    titre = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    date_upload = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)