import dash
from dash import dash_table
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import numpy as np
from scipy.integrate import odeint
import constants
import equations

# Initialize the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout of the app
app.layout = dbc.Container([
    html.H2("Aluminum Electrolysis Process Simulation", className="text-center"),

    dbc.Card([
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    dbc.Label("Time (s)"),
                    dbc.Input(id="input-time", type="number", value=1000),
                ]),
                dbc.Col([
                    dbc.Label("Al2O3 Feed (kg)"),
                    dbc.Input(id="input-u1", type="number", value=np.round(constants.u1_deterministic(constants.cx2),4)),
                ]),
                dbc.Col([
                    dbc.Label("Current (A)"),
                    dbc.Input(id="input-u2", type="number", value=np.round(constants.u2_deterministic(),4)),
                ]),
                dbc.Col([
                    dbc.Label("ALF3 Feed(kg)"),
                    dbc.Input(id="input-u3", type="number", value=np.round(constants.u3_deterministic(constants.cx3),4)),
                ]),
                dbc.Col([
                    dbc.Label("Metal tapping (kg)"),
                    dbc.Input(id="input-u4", type="number", value=np.round(constants.u4_deterministic(constants.x5),0)),
                ]),
                dbc.Col([
                    dbc.Label("Anode Cathode Dist (m)"),
                    dbc.Input(id="input-u5", type="number", value=np.round(constants.u5_deterministic(),2)),
                ]),
            ], className="mb-4"),

            dbc.Row([
                dbc.Col([
                    dbc.Label("Alumina Addition Interval (s)"),
                    dbc.Input(id="input-interval", type="number", value=30),
                ]),
                dbc.Col([
                    dbc.Label("Alumina Addition Amount (kg)"),
                    dbc.Input(id="input-amount", type="number", value=3),
                ]),
            ], className="mb-4"),

            dbc.Row([
                dbc.Col([
                    dbc.Button('Play', id='play-button', className="mb-4 btn-block", color="primary"),
                ], width={"size": 10, "offset": 0}),
            ],justify="left"),
        ]),
    ], className="mb-4"),
    
    html.H4("Intital Condition", className="text-center mb-4"), # Header for state variables

    dbc.Row([
        dbc.Col(
            dash_table.DataTable(
                id='table',
                columns=[{"name": "Variable", "id": "Variable"},
                        {"name": "Initial Value", "id": "Initial Value"}],
                data=[{"Variable": "Mass of side ledge", "Initial Value": constants.x1},
                    {"Variable": "Mass of Al2O3", "Initial Value": constants.x2},
                    {"Variable": "Mass of ALF3", "Initial Value": constants.x3},
                    {"Variable": "Mass of Na3AlF6", "Initial Value": constants.x4},
                    {"Variable": "Mass of metal", "Initial Value": constants.x5},
                    {"Variable": "Temperature of bath", "Initial Value": constants.x6},
                    {"Variable": "Temperature of side ledge", "Initial Value": constants.x7},
                    {"Variable": "Temperature of wall", "Initial Value": constants.x8}],
                style_cell={'maxWidth': '150px'}
            ), 
            width=5, 
            className="mx-auto"
        ),
    ]),
    
    html.H4("State Variables", className="text-center mt-4"), # Header for state variables

    dbc.Row([
        dbc.Col(dcc.Graph(id="output-graph1")),
        dbc.Col(dcc.Graph(id="output-graph2")),
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id="output-graph3")),
        dbc.Col(dcc.Graph(id="output-graph4")),
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id="output-graph5")),
        dbc.Col(dcc.Graph(id="output-graph6")),
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id="output-graph7")),
        dbc.Col(dcc.Graph(id="output-graph8")),
    ]),
    
    html.H3("Control Variables", className="text-center"), # Header for control variables
    
    dbc.Row([
        dbc.Col(dcc.Graph(id="output-graph9")),
        dbc.Col(dcc.Graph(id="output-graph10")),
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id="output-graph11")),
        dbc.Col(dcc.Graph(id="output-graph12")),
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id="output-graph13")),
    ]),
], fluid=True)





@app.callback(
    [Output("output-graph1", "figure"),
     Output("output-graph2", "figure"),
     Output("output-graph3", "figure"),
     Output("output-graph4", "figure"),
     Output("output-graph5", "figure"),
     Output("output-graph6", "figure"),
     Output("output-graph7", "figure"),
     Output("output-graph8", "figure"),
     Output("output-graph9", "figure"),
     Output("output-graph10", "figure"),
     Output("output-graph11", "figure"),
     Output("output-graph12", "figure"),
     Output("output-graph13", "figure")],
    [Input("play-button", "n_clicks"),
     Input("input-interval", "value"),
     Input("input-amount", "value")],
    [State("input-time", "value"),
     State("input-u1", "value"),
     State("input-u2", "value"),
     State("input-u3", "value"),
     State("input-u4", "value"),
     State("input-u5", "value")]
)
def update_graph(n_clicks, time, u1, u2, u3, u4, u5, alumina_interval, alumina_amount):
    if n_clicks is None:
        return [go.Figure() for _ in range(13)]

    x0 = [constants.x1, constants.x2, constants.x3, constants.x4, constants.x5, constants.x6, constants.x7, constants.x8]
    u = [u1, u2, u3, u4, u5]
    constants_values = [constants.k0, constants.k1, constants.k2, constants.k3, constants.k4, constants.k5, constants.k6, constants.k7, constants.k8, constants.k9, constants.k10, constants.k11, constants.k12, constants.k13, constants.k14, constants.k15, constants.k16, constants.k17, constants.k18, constants.alpha, constants.beta]

    t = np.linspace(0, time, alumina_interval)
    x = np.zeros((len(t), len(x0)))
    x[0, :] = x0

    u_values = np.zeros((len(t), len(u)))
    u_values[0, :] = u

    for i in range(len(t)-1):
        if i % (alumina_interval*10) == 0:
            u[0] += alumina_amount
        x_step = odeint(equations.system_odes, x0, [t[i], t[i+1]], args=(u, constants_values))
        x[i+1, :] = x_step[-1, :]
        x0 = x_step[-1, :]
        u_values[i+1, :] = u

    figs = [go.Figure() for _ in range(13)]
    state_names = ['Mass Rate of side ledge (kg/s)', 'Mass of Al2O3', 'Mass of ALF3', 'Mass of Na3AlF6 (kg)', 'Mass of metal (kg)', 'Temperature of bath (°C)', 'Temperature of side ledge (°C)', 'Temperature of wall (°C)']
    control_names = ['Al2O3 Feed (kg)', 'Current (A)', 'ALF3 Feed(kg)', 'Metal tapping (kg)', 'Anode Cathode Dist (m)']

    for i in range(8):
        figs[i].add_trace(go.Scatter(x=t, y=x[:, i], mode='lines', name=state_names[i]))
        figs[i].update_layout(title=state_names[i], xaxis_title='Time (s)', yaxis_title=state_names[i])

    for i in range(5):
        figs[i+8].add_trace(go.Scatter(x=t, y=u_values[:, i], mode='lines', name=control_names[i]))
        figs[i+8].update_layout(title=control_names[i], xaxis_title='Time (s)', yaxis_title=control_names[i])

    return figs

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
