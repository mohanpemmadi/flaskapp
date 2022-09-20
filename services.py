from flask import request

from flask_restful import Resource
from db import get_db_connection

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

class ListAllEmployees(Resource):
    def get(self):
        con = get_db_connection()
        cur = con.cursor()
        cur.execute('select * from employee')
        employees = cur.fetchall()
        data = []
        for row in employees:
            data.append({'name':row[0],'age':row[1],'location':row[2],'sal':row[3]})
        con.close()
        return {'message': 'students data fetched successfully', 'data':data, 'status': 200}

class GetEmployee(Resource):
    def get(self, name):
        con = get_db_connection()
        cur = con.cursor()
        cur.execute("select * from employee where name='{}'".format(name))
        employee = cur.fetchone()
        if employee:
            data = {'name':employee[0],'age':employee[1],'location':employee[2],'sal':employee[3]}
        else:
            return {'message': f'employee {name} data not found '}
        con.close()
        return {'message': f'employee {name} data fetched successfully', 'data':data, 'status': 200}

class CreateEmployee(Resource):
    def post(self):
        req = request.get_json(force=True)
        con = get_db_connection()
        cur = con.cursor()
        insert_query = "insert into employee values('{}',{},'{}',{})".format(req['name'],req['age'],req['location'],req['salary'])
        cur.execute(insert_query)
        con.commit()
        con.close()
        return {'message':'data inserted successfully','status':200}


class UpdateEmployee(Resource):
    def put(self, name):
        req = request.get_json(force=True)
        con = get_db_connection()
        cur = con.cursor()
        update_query = "update employee set age={},location='{}',salary={} where name='{}' ".format(req['age'],req['location'],req['salary'],name)
        cur.execute(update_query)
        con.commit()
        con.close()
        return {'message':f'employee {name} is successfully update','status':200}

class DeleteEmployee(Resource):
    def delete(self, name):
        con = get_db_connection()
        cur = con.cursor()
        delete_query = "delete from employee where name='{}' ".format(name)
        cur.execute(delete_query)
        con.commit()
        con.close()
        return {'message':f'employee {name} is successfully deleted','status':200}




