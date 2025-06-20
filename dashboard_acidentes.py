
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# Carregar os dados reais
df = pd.read_csv("acidentes_transito_brasil.csv")

# Converter a coluna de data
df['data'] = pd.to_datetime(df['data'], format='%Y-%m')

# Agrupar por estado
df_estado = df.groupby('estado')['qtd_vitimas'].sum().reset_index()

# Agrupar por mês
df_mensal = df.groupby('data')['qtd_vitimas'].sum().reset_index()

# Criar o app Dash
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard de Acidentes de Trânsito no Brasil"),

    html.Div([
        html.H3("Total de Acidentes por Estado"),
        dcc.Graph(
            id='grafico-estado',
            figure=px.bar(df_estado, x='estado', y='qtd_vitimas', title='Acidentes por Estado')
        )
    ]),

    html.Div([
        html.H3("Evolução Mensal dos Acidentes"),
        dcc.Graph(
            id='grafico-mensal',
            figure=px.line(df_mensal, x='data', y='qtd_vitimas', title='Acidentes por Mês')
        )
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
