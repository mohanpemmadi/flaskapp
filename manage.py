from flask import Flask
from flask_restful import Api
from urls import all_urls

app = Flask(__name__)
api = Api(app)

all_urls(api)

if __name__ == '__main__':
    app.run(debug=True)