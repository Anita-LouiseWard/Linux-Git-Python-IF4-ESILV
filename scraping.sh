#!/bin/bash

# URL du site web à scrapper
URL="https://fr.timeservers.net/cities/fr/paris"

# Utilisation de curl pour récupérer le contenu de la page web
CONTENT=$(curl -s "$URL")

# Récupération des informations souhaitées en utilisant grep et sed
INFORMATION=$(echo "$CONTENT" | grep "hours" | grep "minutes" | grep "seconds" >

HORAIRE=$(echo "$INFORMATION" | grep -o "[0-9][0-9]:[0-9][0-9]:[0-9][0-9]" | se>

# Affichage des informations récupérées
echo "Les valeurs de l'heure son : $HORAIRE"
