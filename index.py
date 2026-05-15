python
import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load the dataset
data = pd.read_csv('water_consumption_data.csv')

# Initialize Dash app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1('Interactive Water Consumption Dashboard'),
    dcc.Dropdown(
        id='region-dropdown',
        options=[{'label': region, 'value': region} for region in data['Region'].unique()],
        multi=True,
        placeholder='Select Region(s)'
    ),
    dcc.Graph(id='consumption-chart'),
])

# Callback for interactive chart
@app.callback(
    dash.dependencies.Output('consumption-chart', 'figure'),
    [dash.dependencies.Input('region-dropdown', 'value')]
)
def update_chart(selected_regions):
    if not selected_regions:
        filtered_data = data
    else:
        filtered_data = data[data['Region'].isin(selected_regions)]

    fig = px.line(
        filtered_data,
        x='Year',
        y='Water Consumption (Million Cubic Meters)',
        color='Region',
        title='Water Consumption Trends by Region'
    )
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
