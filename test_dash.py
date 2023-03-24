import dash
import dash_html_components as html

# Ouvrir le fichier texte
with open('horaire.txt', 'r') as f:
    #Création de l'historique
    historique = []
    # Lire chaque ligne du fichier
    for line in f:
        # Extraire l'heure
        heure = line[:2]

with open('horaire.txt', 'r') as f:
    # Lire chaque ligne du fichier
    for line in f:
        # Extraire les minutes
        minutes = line[2:4]

heure_minute = heure + "H" + minutes
historique.append(heure_minute)

app = dash.Dash(__name__)

app.layout = html.Div(children = [
    html.H1(f"A paris, il est actuellement : {heure}h{minutes}"),
    html.H2("Historique :"),
    html.Ul([html.Li(historique[i]) for i in range(len(historique))])
])

app.run_server(debug=True, host='0.0.0.0')
