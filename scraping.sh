#!/bin/bash

# URL du site web à scrapper
URL="https://fr.timeservers.net/cities/fr/paris"

# Utilisation de curl pour récupérer le contenu de la page web
CONTENT=$(curl -s "$URL")

# Récupération des informations souhaitées en utilisant grep et sed
INFORMATION=$(echo "$CONTENT" | grep "hours" | grep "minutes" | grep "seconds" | sed 's/<[^>]*>//g')

HORAIRE=$(echo "$INFORMATION" | grep -o "[0-9][0-9]:[0-9][0-9]:[0-9][0-9]" | sed 's/://g')

SUNSET=$(echo "$CONTENT" | grep "city.sunset")

# Affichage des informations récupérées
echo "Les valeurs de l'heure sont : $HORAIRE"
echo "$HORAIRE" >> horaire.txt
echo "$SUNSET" > sunset.txt

# Récupérer la dernière ligne du fichier sunset.txt
last_line=$(tail -n 1 sunset.txt)

# Extraire la valeur de "sunset" à partir de la dernière ligne
SUNSET=$(echo $last_line | grep -oP '(?<=sunset">)[0-9]{2}:[0-9]{2}')

echo "Le soleil se couche à : $SUNSET"
echo "$SUNSET" > sunset.txt

LINES=$(wc -l < horaire.txt)
if [ $LINES -gt 10 ]; then
  sed -i '1d' horaire.txt
fi
