from flask_restful import Resource

class HelloWorld(Resource):
    def get(self):
        return {'message': 'welcome to flask app'}

class Home(Resource):
    def get(self):
        return {'message': 'Home page!'}

class MyName(Resource):
    def get(self, name):
        return {'message':f'Hello {name}, Welcome to flask app'}

class MyAge(Resource):
    def get(self, age):
        return {'message':f'Hello guys, my age is {age}'}

class ListAllData(Resource):
    def get(self):
        pass
