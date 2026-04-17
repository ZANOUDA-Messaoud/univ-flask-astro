#!/usr/bin/env python3
"""
Script pour exporter les données de SQLite vers JSON
avant la migration vers MariaDB
"""
import json
from app import app
from models import db, User, Appareil, Telescope, Photo
from werkzeug.security import generate_password_hash

def export_data():
    """Exporte toutes les données de la BD SQLite en JSON"""
    
    with app.app_context():
        # Récupérer toutes les données
        users = User.query.all()
        appareils = Appareil.query.all()
        telescopes = Telescope.query.all()
        photos = Photo.query.all()
        
        # Conversion en dictionnaires
        data = {
            'users': [
                {
                    'id': u.id,
                    'username': u.username,
                    'password': u.password  # Hash déjà présent
                }
                for u in users
            ],
            'appareils': [
                {
                    'id': a.id,
                    'marque': a.marque,
                    'modele': a.modele,
                    'date_sortie': a.date_sortie,
                    'score': a.score,
                    'categorie': a.categorie
                }
                for a in appareils
            ],
            'telescopes': [
                {
                    'id': t.id,
                    'marque': t.marque,
                    'modele': t.modele,
                    'date_sortie': t.date_sortie,
                    'score': t.score,
                    'categorie': t.categorie
                }
                for t in telescopes
            ],
            'photos': [
                {
                    'id': p.id,
                    'filename': p.filename,
                    'titre': p.titre,
                    'description': p.description,
                    'date_upload': p.date_upload.isoformat() if p.date_upload else None,
                    'user_id': p.user_id
                }
                for p in photos
            ]
        }
        
        # Exporter en JSON
        with open('data_backup.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print("✅ Données exportées vers data_backup.json")
        print(f"   - {len(users)} utilisateurs")
        print(f"   - {len(appareils)} appareils")
        print(f"   - {len(telescopes)} télescopes")
        print(f"   - {len(photos)} photos")

if __name__ == '__main__':
    export_data()
