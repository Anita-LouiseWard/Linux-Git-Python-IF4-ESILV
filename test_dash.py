import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import time
import subprocess
import schedule

def print_sunset():
    with open('sunset.txt', 'r') as f:
        sunset = f.read().strip()
        return html.Div(f"Le coucher de soleil est à {sunset}")

schedule.every().day.at("17:15").do(print_sunset)

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
        historique = [line.strip() for line in lines[-10:][::-1]]

    heure_minute = heure + "H" + minutes
    #historique.append(heure_minute)

    return html.Div(children = [
        html.H1(f"A paris, il est actuellement : {heure}h{minutes}"),
        html.H2("Les 10 derniers horaires récupérés sont :"),
        html.Ul([html.Li(historique[i]) for i in range(len(historique))])
    ])

app = dash.Dash(__name__)

app.layout = html.Div(children = [
    html.Div(id='horaires-div'),
    html.Div(id='sunset-div'),
    dcc.Interval(
        id='interval-component',
        interval=30*1000, # en millisecondes
        n_intervals=0
    )
])

@app.callback(
    Output('horaires-div', 'children'),
    [Input('interval-component', 'n_intervals')])
def update_horaires_div(n):
    subprocess.call(["bash", "scraping.sh"]) # Exécute le script bash à chaque mise à jour
    return html.Div([
        update_horaires(),
        html.H3(print_sunset())
    ]),

@app.callback(
    Output('sunset-div', 'children'),
    [Input('interval-component', 'n_intervals')])
def update_sunset_div(n):
    if time.strftime("%H:%M") == "17:15":
        return print_sunset()
    else:
        return ""

if __name__ == '__main__':
    schedule.every().day.at("17:15").do(print_sunset)
    app.run_server(debug=True, host='0.0.0.0')
