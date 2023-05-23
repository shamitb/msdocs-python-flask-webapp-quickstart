from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    access_token = request.headers.get('Authorization')
    user_principal = request.headers.get('X-User-Principal')

    #if access_token:
    # Use the access token for further validation or authorization
    print(dict(request.headers))

    return "Request received"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
