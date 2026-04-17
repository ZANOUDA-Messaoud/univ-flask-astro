# Configuration Flask pour MariaDB
# Remplacez config.py avec cette configuration pour utiliser MariaDB

import os

# ========== CONFIGURATION MARIADB ==========
# Pour utiliser MariaDB au lieu de SQLite, décommentez les lignes ci-dessous
# et installez le driver : pip install pymysql

# Option 1 : Utiliser PyMySQL (recommandé pour développement)
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://astro_user:astro_password@localhost/astro_db"

# Option 2 : Utiliser MySQLdb (nécessite sudo apt install python3-mysqldb)
# SQLALCHEMY_DATABASE_URI = "mysql://astro_user:astro_password@localhost/astro_db"

# Configuration commune
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENGINE_OPTIONS = {
    'pool_size': 10,
    'pool_recycle': 3600,
    'pool_pre_ping': True,
}

SECRET_KEY = "supersecretkey"
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static', 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max
