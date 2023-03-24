import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import time
import subprocess

def update_horaires():
    # Récupérer la dernière lignes du fichier texte
    with open('horaire.txt', 'r') as f:
        lines = f.readlines()
        last_line = lines[-1].strip()
        # Récupère les heures dans la dernière ligne de horaire.txt
        heure = last_line[:2]
        # Récupère les minutes dans la dernière ligne de horaire.txt
        minutes = last_line[2:4]
        # Création de l'historique
        historique = []

    heure_minute = heure + "H" + minutes
    historique.append(heure_minute)

    return html.Div(children = [
        html.H1(f"A paris, il est actuellement : {heure}h{minutes}"),
        html.H2("Les 10 derniers horaires récupérés sont :"),
        html.Ul([html.Li(historique[i]) for i in range(len(historique))])
    ])

app = dash.Dash(__name__)

app.layout = html.Div(children = [
    html.Div(id='horaires-div'),
    dcc.Interval(
        id='interval-component',
        interval=5*1000, # en millisecondes
        n_intervals=0
    )
])

@app.callback(
    Output('horaires-div', 'children'),
    [Input('interval-component', 'n_intervals')])
def update_horaires_div(n):
    subprocess.call(["bash", "scraping.sh"]) # Exécute le script bash à chaque mise à jour
    return update_horaires()

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')
