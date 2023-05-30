import dash
from dash.dependencies import Input, Output
import flask

app = dash.Dash(__name__)

# Define a callback function that retrieves the client principal name
@app.callback(Output('output', 'children'), [Input('dummy-input', 'value')])
def get_client_principal_name(dummy_value):
    # Get the request context from the global Flask object
    ctx = flask._app_ctx_stack.top

    # Check if the request context exists
    if ctx is not None:
        # Access the request headers
        request = flask.request
        headers = request.headers

        # Retrieve the client principal name from the headers
        principal_name = headers.get('X-Ms-Client-Principal-Name')

        if principal_name:
            return f"Client Principal Name: {principal_name}"

    # Return a default value if the client principal name is not found
    return "Client Principal Name not found."

# Define the layout of the app
app.layout = dash.html.Div([
    dash.dcc.Input(id='dummy-input', style={'display': 'none'}),
    dash.html.Div(id='output')
])

if __name__ == '__main__':
    app.run_server(debug=True)
