#!/bin/bash
"""
Script d'installation et configuration de MariaDB
Exécutez avec : bash setup_mariadb.sh
"""

echo "=== Installation de MariaDB ==="
echo "Mise à jour des repos..."
sudo apt update

echo "Installation de MariaDB..."
sudo apt install mariadb-server -y

echo "Démarrage du service MariaDB..."
sudo service mariadb start

echo ""
echo "=== Configuration de sécurité ==="
echo "Veuillez répondre aux questions de sécurité :"
echo "- Root password: laisser vide ou définir"
echo "- Remove anonymous users: Y"
echo "- Disable remote root: Y"
echo "- Remove test database: Y"
echo "- Reload privileges: Y"
echo ""
sudo mysql_secure_installation

echo ""
echo "=== Création de la base de données ==="
sudo mysql -u root -p -e "
CREATE DATABASE IF NOT EXISTS astro_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER IF NOT EXISTS 'astro_user'@'localhost' IDENTIFIED BY 'astro_password';
GRANT ALL PRIVILEGES ON astro_db.* TO 'astro_user'@'localhost';
FLUSH PRIVILEGES;
"

echo "✅ MariaDB installé et configuré!"
echo ""
echo "Informations de connexion :"
echo "- Host: localhost"
echo "- Database: astro_db"
echo "- User: astro_user"
echo "- Password: astro_password"
