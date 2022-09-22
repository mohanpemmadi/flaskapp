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

class ListEmployees(Resource):
    def get(self):
        emp_data = Employee.query.all() # query set
        # print('emp_data : ', emp_data)
        res_list = []
        for emp in emp_data:
            res_list.append({'id':emp.id,'name':emp.name,'age':emp.age,'location':emp.location,'salary':emp.salary})
        return {'data':res_list}

class UpdateEmployees(Resource):
    def put(self, id):
        req_body = request.get_json()
        emp = Employee.query.get(id)
        if emp is not None:
            emp.name = req_body['name']
            emp.age = req_body['age']
            emp.location = req_body['location']
            emp.salary = req_body['salary']
            db.session.commit()
            return {'data':{'id':emp.id,'name':emp.name,'age':emp.age,'location':emp.location,'salary':emp.salary}}
        else:
            return {'message': f'employee id {id} does not exists'}

class DeleteEmployees(Resource):
    def delete(self, id):
        emp = Employee.query.get(id)
        if emp is not None:
            db.session.delete(emp)
            db.session.commit()
            return {'message': f'Employee {emp.name} deleted successfully'}
        else:
            return {'message': f'Employee id {id} does not exists'}

class GetEmployee(Resource):
    def get(self, id):
        emp = Employee.query.get(id)
        return {'data':{'id':emp.id,'name':emp.name,'age':emp.age,'salary':emp.salary,'location':emp.location}}


api.add_resource(AddEmployee, '/add_new_employee')
api.add_resource(ListEmployees, '/list_employees')
api.add_resource(UpdateEmployees, '/update_emp/<int:id>')
api.add_resource(DeleteEmployees, '/delete_emp/<int:id>')
api.add_resource(GetEmployee, '/get_employee/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)