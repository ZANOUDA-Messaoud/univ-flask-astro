#!/usr/bin/env python3
"""
Script pour importer les données JSON dans MariaDB
après la migration depuis SQLite
"""
import json
from datetime import datetime
from app import app
from models import db, User, Appareil, Telescope, Photo

def import_data(filename='data_backup.json'):
    """Importe les données depuis un fichier JSON"""
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        with app.app_context():
            # Importer les utilisateurs
            print("📥 Import des utilisateurs...")
            for user_data in data.get('users', []):
                existing = User.query.filter_by(id=user_data['id']).first()
                if not existing:
                    user = User(
                        id=user_data['id'],
                        username=user_data['username'],
                        password=user_data['password']
                    )
                    db.session.add(user)
            db.session.commit()
            print(f"✅ {len(data.get('users', []))} utilisateurs importés")
            
            # Importer les appareils
            print("📥 Import des appareils...")
            for appareil_data in data.get('appareils', []):
                existing = Appareil.query.filter_by(id=appareil_data['id']).first()
                if not existing:
                    appareil = Appareil(
                        id=appareil_data['id'],
                        marque=appareil_data['marque'],
                        modele=appareil_data['modele'],
                        date_sortie=appareil_data['date_sortie'],
                        score=appareil_data['score'],
                        categorie=appareil_data['categorie']
                    )
                    db.session.add(appareil)
            db.session.commit()
            print(f"✅ {len(data.get('appareils', []))} appareils importés")
            
            # Importer les télescopes
            print("📥 Import des télescopes...")
            for telescope_data in data.get('telescopes', []):
                existing = Telescope.query.filter_by(id=telescope_data['id']).first()
                if not existing:
                    telescope = Telescope(
                        id=telescope_data['id'],
                        marque=telescope_data['marque'],
                        modele=telescope_data['modele'],
                        date_sortie=telescope_data['date_sortie'],
                        score=telescope_data['score'],
                        categorie=telescope_data['categorie']
                    )
                    db.session.add(telescope)
            db.session.commit()
            print(f"✅ {len(data.get('telescopes', []))} télescopes importés")
            
            # Importer les photos
            print("📥 Import des photos...")
            for photo_data in data.get('photos', []):
                existing = Photo.query.filter_by(id=photo_data['id']).first()
                if not existing:
                    date_upload = None
                    if photo_data.get('date_upload'):
                        try:
                            date_upload = datetime.fromisoformat(photo_data['date_upload'])
                        except:
                            date_upload = datetime.now()
                    
                    photo = Photo(
                        id=photo_data['id'],
                        filename=photo_data['filename'],
                        titre=photo_data['titre'],
                        description=photo_data['description'],
                        date_upload=date_upload,
                        user_id=photo_data['user_id']
                    )
                    db.session.add(photo)
            db.session.commit()
            print(f"✅ {len(data.get('photos', []))} photos importées")
            
            print("\n✅ Import terminé avec succès!")
            
    except FileNotFoundError:
        print(f"❌ Erreur : fichier '{filename}' non trouvé")
        print("Avez-vous exécuté export_data.py d'abord ?")
    except Exception as e:
        print(f"❌ Erreur lors de l'import : {e}")
        db.session.rollback()

if __name__ == '__main__':
    import_data()
