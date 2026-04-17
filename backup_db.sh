#!/bin/bash
# Script pour sauvegarder la base de données MariaDB

echo "=== Sauvegarde de la base de données MariaDB ==="
echo ""

# Variables
DB_USER="astro_user"
DB_PASS="astro_password"
DB_NAME="astro_db"
BACKUP_DIR="/workspaces/univ-flask-astro"
DATE=$(date +%Y%m%d_%H%M%S)

# Noms des fichiers de sauvegarde
SCHEMA_FILE="$BACKUP_DIR/schema_$DATE.sql"
DATA_FILE="$BACKUP_DIR/data_$DATE.sql"
FULL_FILE="$BACKUP_DIR/astro_db_backup_$DATE.sql"

# Vérifier que MariaDB est accessible
echo "Vérification de la connexion à MariaDB..."
mysql -u "$DB_USER" -p"$DB_PASS" -e "SELECT VERSION();" > /dev/null 2>&1

if [ $? -ne 0 ]; then
    echo "❌ Erreur : Impossible de se connecter à MariaDB"
    echo "Vérifiez :"
    echo "  - Que MariaDB est en cours d'exécution : sudo service mariadb status"
    echo "  - Les identifiants (user: $DB_USER, db: $DB_NAME)"
    exit 1
fi

echo "✅ Connexion établie"
echo ""

# Exporter le schéma (structure sans données)
echo "📥 Export du schéma..."
mysqldump -u "$DB_USER" -p"$DB_PASS" --no-data "$DB_NAME" > "$SCHEMA_FILE"
if [ $? -eq 0 ]; then
    SIZE=$(du -h "$SCHEMA_FILE" | cut -f1)
    echo "✅ Schéma exporté : $SCHEMA_FILE ($SIZE)"
else
    echo "❌ Erreur lors de l'export du schéma"
    exit 1
fi

echo ""

# Exporter les données uniquement
echo "📥 Export des données..."
mysqldump -u "$DB_USER" -p"$DB_PASS" --no-create-info "$DB_NAME" > "$DATA_FILE"
if [ $? -eq 0 ]; then
    SIZE=$(du -h "$DATA_FILE" | cut -f1)
    echo "✅ Données exportées : $DATA_FILE ($SIZE)"
else
    echo "❌ Erreur lors de l'export des données"
    exit 1
fi

echo ""

# Exporter tout en un
echo "📥 Export complet (schéma + données)..."
mysqldump -u "$DB_USER" -p"$DB_PASS" "$DB_NAME" > "$FULL_FILE"
if [ $? -eq 0 ]; then
    SIZE=$(du -h "$FULL_FILE" | cut -f1)
    echo "✅ Backup complet : $FULL_FILE ($SIZE)"
else
    echo "❌ Erreur lors de l'export complet"
    exit 1
fi

echo ""
echo "=== Résumé ==="
echo "✅ Tous les fichiers ont été créés avec succès!"
echo ""
echo "Fichiers créés :"
echo "  1. Schéma seul    : $SCHEMA_FILE"
echo "  2. Données seules : $DATA_FILE"
echo "  3. Complet        : $FULL_FILE"
echo ""
echo "📋 Pour restaurer la base de données :"
echo "  mysql -u $DB_USER -p$DB_PASS $DB_NAME < $FULL_FILE"
