# Guide de Migration SQLite → MariaDB

## 📋 Étapes de migration

### 1️⃣ Exporter les données SQLite
```bash
python export_data.py
```
Cela crée un fichier `data_backup.json` avec toutes les données.

### 2️⃣ Installer MariaDB
```bash
bash setup_mariadb.sh
```

### 3️⃣ Installer le driver PyMySQL
```bash
pip install -r requirements_mariadb.txt
```

### 4️⃣ Mettre à jour la configuration Flask
Remplacez le contenu de `config.py` par le contenu de `config_mariadb.py` :
```bash
cp config_mariadb.py config.py
```

### 5️⃣ Créer les tables dans MariaDB
```bash
python -c "from app import app, db; app.app_context().push(); db.create_all()"
```

### 6️⃣ Importer les données
```bash
python import_data.py
```

### 7️⃣ Vérifier l'import
```bash
python -c "from app import app; from models import User, Photo; app.app_context().push(); print('Users:', User.query.count(), 'Photos:', Photo.query.count())"
```

---

## 🔧 Configuration MariaDB

**Identifiants créés :**
- User: `astro_user`
- Password: `astro_password`
- Database: `astro_db`
- Host: `localhost`

⚠️ **À changer en production** avec des identifiants sécurisés!

---

## 💾 Sauvegarde et export finaux

Avant de rendre votre code :

```bash
# 1. Exporter le schéma
sudo mysqldump -u astro_user -p --no-data astro_db > schema.sql

# 2. Exporter les données
sudo mysqldump -u astro_user -p astro_db > data.sql

# 3. Exporter tout en un
sudo mysqldump -u astro_user -p astro_db > astro_db_backup.sql
```

---

## 🔄 Revenir à SQLite (si nécessaire)

```bash
# Restaurer le fichier config.py original
git checkout config.py

# Vérifier que la BD SQLite est présente
python -c "from app import app, db; app.app_context().push(); print('Tables:', db.metadata.tables.keys())"
```

---

## 📝 Notes importantes

- ✅ Les données SQLite restent intactes pendant la migration
- ✅ Vous pouvez tester avant de commencer l'import complet
- ⚠️ Assurez-vous que MariaDB est en cours d'exécution avant de lancer l'app
- ⚠️ Exporter `data_backup.json` et les fichiers SQL avant de rendre le code

---

## ⚠️ Variables d'environnement (recommandé)

Pour plus de sécurité, utilisez un fichier `.env` :

```bash
# .env
DATABASE_URL=mysql+pymysql://astro_user:astro_password@localhost/astro_db
SECRET_KEY=your-secret-key
```

Et mettez à jour `config.py` :
```python
import os
from dotenv import load_dotenv

load_dotenv()
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
```
