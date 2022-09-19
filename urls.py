# from services import Home, HelloWorld, MyName, MyAge

import services
# from services import *

def all_urls(api):
    api.add_resource(services.HelloWorld, '/welcome') # http://127.0.0.1:5000/welcome
    api.add_resource(services.Home, '/home') # http://127.0.0.1:5000/home
    api.add_resource(services.MyName, '/myname/<string:name>') #  http://127.0.0.1:5000/myname/mohan
    api.add_resource(services.MyAge, '/myage/<int:age>')
    api.add_resource(services.ListAllEmployees,'/list_all_emp') #  http://127.0.0.1:5000/list_all_students
    api.add_resource(services.CreateEmployee,'/add_employee') #  http://127.0.0.1:5000/add_employee