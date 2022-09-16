from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'message': 'welcome to flask app'}

class Home(Resource):
    def get(self):
        return {'message': 'Home page!'}

api.add_resource(HelloWorld, '/welcome') # http://127.0.0.1:5000/welcome
api.add_resource(Home, '/home') # http://127.0.0.1:5000/home


if __name__ == '__main__':
    app.run(debug=True)