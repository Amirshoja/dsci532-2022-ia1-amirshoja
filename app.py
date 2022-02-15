from vega_datasets import data
import altair as alt
from dash import Dash, html, dcc, Input, Output

# loading the cars data
movies = data.movies()

app = Dash(
    __name__, external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"]
)

server = app.server

app.layout = html.Div(
    [
        html.Iframe(
            id="scatter",
            style={"border-width": "0", "width": "100%", "height": "400px"},
        ),
        dcc.Dropdown(
            id="xcol-widget",
            value="Production_Budget",
            options=[{"label": col, "value": col} for col in movies.columns],
        ),
    ]
)


@app.callback(Output("scatter", "srcDoc"), Input("xcol-widget", "value"))
def plot_movies(xcol):
    chart = (
        alt.Chart(movies)
        .mark_point()
        .encode(x=xcol, y="Worldwide_Gross", tooltip="Title")
        .interactive()
    )
    return chart.to_html()


if __name__ == "__main__":
    app.run_server(debug=True)


data.list_datasets()
