from flask import Flask, render_template, request, redirect, session, send_from_directory
from models import db, User, Appareil, Telescope, Photo
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
from datetime import datetime

app = Flask(__name__)
app.config.from_object("config")

db.init_app(app)

# Créer le dossier uploads s'il n'existe pas
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Vérifie si une extension de fichier est autorisée
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route("/")
def home():
    if "user_id" not in session:
        return redirect("/login")   #Si l'utilisateur n'est pas connecté
    return redirect("/appareils")   #Si l'utilisateur est pas connecté

    # Créer un nouvel utilisateur
@app.route("/register", methods=["GET", "POST"]) #GET pour afficher le formulaire d'inscription, POST pour traiter les données du formulaire
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()

        return redirect("/login")

    return render_template("register.html")


    #Authentification de l'utilisateur
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(username=request.form["username"]).first()

        if user and check_password_hash(user.password, request.form["password"]):
            session["user_id"] = user.id
            return redirect("/")

    return render_template("login.html")

    #Déconnexion de l'utilisateur
@app.route("/logout")
def logout():
    session.clear() #Efface toutes les données de session, y compris l'ID de l'utilisateur
    return redirect("/login")   #Redirige vers la page de connexion après la déconnexion


    #Affichage des appareils et des télescopes
@app.route("/appareils")
def appareils():
    if "user_id" not in session:
        return redirect("/login")
    data = Appareil.query.all()
    return render_template("appareils.html", appareils=data)    #Récupère tous les appareils de la base de données et les affiche dans le template appareils.html

    #Affichage des télescopes
@app.route("/telescopes")
def telescopes():
    if "user_id" not in session:
        return redirect("/login")
    data = Telescope.query.all()    #Récupère tous les télescopes de la base de données et les affiche dans le template telescopes.html
    return render_template("telescopes.html", telescopes=data)  #Affichage des photos de l'utilisateur connecté et gestion de l'upload de nouvelles photos

    #Affichage des photos de l'utilisateur connecté et gestion de l'upload de nouvelles photos
@app.route("/photos", methods=["GET", "POST"])
def photos():
    if "user_id" not in session:    #Si l'user n'est pas connecté, redirige vers la page de connexion
        return redirect("/login")
    
    if request.method == "POST":    #Vérifie si un fichier a été envoyé dans la requête POST, sinon redirige vers la page des photos
        if 'file' not in request.files:
            return redirect("/photos")
        
        file = request.files['file']
        titre = request.form.get('titre', 'Sans titre')
        description = request.form.get('description', '')
        
        if file and file.filename and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_')
            filename = timestamp + filename
            
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            photo = Photo(
                filename=filename,
                titre=titre,
                description=description,
                user_id=session["user_id"]
            )
            db.session.add(photo)
            db.session.commit()
            
            return redirect("/photos")
    
    user_photos = Photo.query.order_by(Photo.date_upload.desc()).all()
    return render_template("photos.html", photos=user_photos)   
    #Récupère les photos de l'utilisateur connecté, les trie par date de téléchargement décroissante et les affiche dans le template photos.html

    #Route pour servir les fichiers téléchargés
@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], secure_filename(filename))  
    #Permet de servir les fichiers téléchargés en utilisant le nom de fichier sécurisé pour éviter les problèmes de sécurité liés aux chemins de fichiers.

if __name__ == "__main__":
    app.run(debug=True)