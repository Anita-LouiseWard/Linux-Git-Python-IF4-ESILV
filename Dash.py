import dash
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(children = [
    html.H1("Demo"),
    html.H2("Test")
])

app.run_server(debug=True)
