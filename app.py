from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

# host='localhost'
# database='flaskdb'
# username='postgres'
# password='root'
# port='5432'

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://postgres:root@localhost:5432/flaskdb"
# app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{username}:{password}@{host}:{port}/{database}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
api = Api(app)

# create an employee model

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    location = db.Column(db.String(150), nullable=False)
    salary = db.Column(db.Float)

class AddEmployee(Resource):
    def post(self):
        req = request.get_json()
        emp = Employee(name=req['name'],age=req['age'],location=req['location'],salary=req['salary'])
        db.session.add(emp)
        db.session.commit()
        emp_data = {'id':emp.id,'name':emp.name,'age':emp.age,'location':emp.location,'salary':emp.salary}
        return {'message':f'Employee {emp.name} added', 'data':emp_data, 'status':200}


api.add_resource(AddEmployee, '/add_new_employee')
api.add_resource(AddEmployee, '/get_all_employees')

if __name__ == '__main__':
    app.run(debug=True)