from app import app
from models import db, User, Appareil, Telescope, Photo
from werkzeug.security import generate_password_hash
import os
import urllib.request

sample_users = [
    {"username": "astronome", "password": "astro123"},
    {"username": "observateur", "password": "galaxie"}
]

sample_appareils = [
    {"marque": "Sony", "modele": "Alpha A7 III", "date_sortie": "2018", "score": 5, "categorie": "mirrorless"},
    {"marque": "Nikon", "modele": "D850", "date_sortie": "2017", "score": 4, "categorie": "DSLR"},
    {"marque": "Canon", "modele": "EOS R6", "date_sortie": "2020", "score": 5, "categorie": "mirrorless"}
]

sample_telescopes = [
    {"marque": "Celestron", "modele": "NexStar 8SE", "date_sortie": "2014", "score": 4, "categorie": "Schmidt-Cassegrain"},
    {"marque": "Sky-Watcher", "modele": "Skymax 127", "date_sortie": "2016", "score": 4, "categorie": "Maksutov-Cassegrain"},
    {"marque": "Orion", "modele": "SkyQuest XT10", "date_sortie": "2015", "score": 5, "categorie": "Dobsonian"}
]

sample_photos = [
    {
        "titre": "Lune brillante",
        "description": "Belle photo de la lune en haute résolution",
        "user": 1,
        "url": "https://images.unsplash.com/photo-1419242902214-272b3f66ee7a?w=800&q=80"
    },
    {
        "titre": "Orion",
        "description": "La constellation d'Orion capturée avec mon télescope",
        "user": 1,
        "url": "https://images.unsplash.com/photo-1419242902214-272b3f66ee7a?w=800&q=80"
    },
    {
        "titre": "Voie Lactée",
        "description": "Magnifique vue de la Voie Lactée au-dessus des montagnes",
        "user": 2,
        "url": "https://images.unsplash.com/photo-1446776877081-d282a0f896e2?w=800&q=80"
    },
    {
        "titre": "Éclipse Solaire",
        "description": "Éclipse solaire totale en grand-angle",
        "user": 2,
        "url": "https://images.unsplash.com/photo-1446776653964-20c1d3a81b06?w=800&q=80"
    }
]

def download_image(url, filename):
    """Télécharger une image depuis une URL"""
    try:
        print(f"  Téléchargement: {filename}...", end=" ")
        urllib.request.urlretrieve(url, filename)
        size = os.path.getsize(filename) / 1024
        print(f"✓ ({size:.1f} KB)")
        return True
    except Exception as e:
        print(f"✗ Erreur: {e}")
        return False

with app.app_context():
    for user_data in sample_users:
        if not User.query.filter_by(username=user_data["username"]).first():
            user = User(
                username=user_data["username"],
                password=generate_password_hash(user_data["password"])
            )
            db.session.add(user)

    db.session.commit()

    for appareil_data in sample_appareils:
        if not Appareil.query.filter_by(marque=appareil_data["marque"], modele=appareil_data["modele"]).first():
            db.session.add(Appareil(**appareil_data))

    for telescope_data in sample_telescopes:
        if not Telescope.query.filter_by(marque=telescope_data["marque"], modele=telescope_data["modele"]).first():
            db.session.add(Telescope(**telescope_data))

    db.session.commit()

    print("\n📸 Téléchargement des images d'Unsplash...")
    for idx, photo_data in enumerate(sample_photos):
        if not Photo.query.filter_by(titre=photo_data["titre"]).first():
            filename = f"sample_{idx}.jpg"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            
            if download_image(photo_data["url"], filepath):
                photo = Photo(
                    filename=filename,
                    titre=photo_data["titre"],
                    description=photo_data["description"],
                    user_id=photo_data["user"]
                )
                db.session.add(photo)
    
    db.session.commit()
    print("\n✓ Seed data has been added to the database.")
