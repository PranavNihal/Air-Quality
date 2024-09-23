import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import random

# Create Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


# Simulate sensor data generation
def generate_data():
    return {
        'Temperature': random.uniform(20, 30),
        'Pressure': random.uniform(990, 1020),
        'Humidity': random.uniform(40, 60),
        'VOCs': random.uniform(0.1, 0.5),
        'Altitude': random.uniform(100, 150),
        'MQ7-CO': random.uniform(0, 10),
        'MQ135-CO': random.uniform(0, 10),
        'CO2': random.uniform(300, 600),
        'Alcohol': random.uniform(0, 0.5),
        'Toluene': random.uniform(0, 0.5),
        'NH4': random.uniform(0, 0.5),
        'Acetone': random.uniform(0, 0.5),
    }


# Define layout
app.layout = dbc.Container([
    html.H1("Air Quality Monitoring System", className="text-center my-4"),

    # Cards for sensor readings
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("Temperature (°C)", className="card-title"),
                html.H3(id='temperature', className="card-text"),
            ])
        ], color="primary", inverse=True)),

        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("Pressure (hPa)", className="card-title"),
                html.H3(id='pressure', className="card-text"),
            ])
        ], color="success", inverse=True)),

        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("Humidity (%)", className="card-title"),
                html.H3(id='humidity', className="card-text"),
            ])
        ], color="info", inverse=True)),
    ], className="mb-4"),

    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("VOCs (ppm)", className="card-title"),
                html.H3(id='vocs', className="card-text"),
            ])
        ], color="warning", inverse=True)),

        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("Altitude (m)", className="card-title"),
                html.H3(id='altitude', className="card-text"),
            ])
        ], color="danger", inverse=True)),
    ], className="mb-4"),

    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("MQ7-CO (ppm)", className="card-title"),
                html.H3(id='mq7_co', className="card-text"),
            ])
        ], color="secondary", inverse=True)),

        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("MQ135-CO (ppm)", className="card-title"),
                html.H3(id='mq135_co', className="card-text"),
            ])
        ], color="dark", inverse=True)),

        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("CO2 (ppm)", className="card-title"),
                html.H3(id='co2', className="card-text"),
            ])
        ], color="primary", inverse=True)),
    ], className="mb-4"),

    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("Alcohol (ppm)", className="card-title"),
                html.H3(id='alcohol', className="card-text"),
            ])
        ], color="success", inverse=True)),

        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("Toluene (ppm)", className="card-title"),
                html.H3(id='toluene', className="card-text"),
            ])
        ], color="info", inverse=True)),

        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("NH4 (ppm)", className="card-title"),
                html.H3(id='nh4', className="card-text"),
            ])
        ], color="warning", inverse=True)),

        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("Acetone (ppm)", className="card-title"),
                html.H3(id='acetone', className="card-text"),
            ])
        ], color="danger", inverse=True)),
    ], className="mb-4"),

    # Interval to update data every 5 seconds
    dcc.Interval(id='interval', interval=5000, n_intervals=0)
])


# Update function for all sensors
@app.callback(
    [Output('temperature', 'children'),
     Output('pressure', 'children'),
     Output('humidity', 'children'),
     Output('vocs', 'children'),
     Output('altitude', 'children'),
     Output('mq7_co', 'children'),
     Output('mq135_co', 'children'),
     Output('co2', 'children'),
     Output('alcohol', 'children'),
     Output('toluene', 'children'),
     Output('nh4', 'children'),
     Output('acetone', 'children')],
    [Input('interval', 'n_intervals')]
)
def update_data(n):
    data = generate_data()
    return (f"{data['Temperature']:.2f}",
            f"{data['Pressure']:.2f}",
            f"{data['Humidity']:.2f}",
            f"{data['VOCs']:.2f}",
            f"{data['Altitude']:.2f}",
            f"{data['MQ7-CO']:.2f}",
            f"{data['MQ135-CO']:.2f}",
            f"{data['CO2']:.2f}",
            f"{data['Alcohol']:.2f}",
            f"{data['Toluene']:.2f}",
            f"{data['NH4']:.2f}",
            f"{data['Acetone']:.2f}")


# Run app
if __name__ == '__main__':
    app.run_server(debug=True)
